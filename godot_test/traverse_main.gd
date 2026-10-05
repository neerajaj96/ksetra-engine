extends Node3D
# Traverse proof: the east axis is walkable from outside Maryada to the
# sanctum door, where SanctumBarrier (K-TANTRI-ONLY) holds. No player needed:
# physics rays walk the route a devotee would take.
const Builder = preload("res://godot/ksetra_builder.gd")

var _errs: Array = []

func _ray(from: Vector3, to: Vector3, label: String, expect_hit: bool, want_name := "") -> Dictionary:
	var q := PhysicsRayQueryParameters3D.create(from, to)
	var hit := get_world_3d().direct_space_state.intersect_ray(q)
	var got := not hit.is_empty()
	if got != expect_hit:
		_errs.append("%s: expected hit=%s got=%s" % [label, str(expect_hit), str(got)])
		return {}
	if expect_hit and want_name != "":
		var col: Object = hit["collider"]
		var n: Node = col as Node
		while n != null and str(n.name) != want_name and n.get_parent() != null:
			n = n.get_parent()
		if n == null or str(n.name) != want_name:
			var found := "?"
			if col is Node:
				found = str((col as Node).name)
			_errs.append("%s: hit %s, wanted %s" % [label, found, want_name])
	return hit

func _floor(x: float, z: float, want_y: float, label: String) -> void:
	var hit := _ray(Vector3(x, 5, z), Vector3(x, -1, z), label, true)
	if not hit.is_empty():
		var hy: float = (hit["position"] as Vector3).y
		if absf(hy - want_y) > 0.08:
			_errs.append("%s: floor y=%.2f want %.2f" % [label, hy, want_y])

func _find_node(n: Node, nm: String) -> Node:
	if str(n.name) == nm:
		return n
	for c in n.get_children():
		var hit := _find_node(c, nm)
		if hit != null:
			return hit
	return null

func _check_sopana(b: Node) -> void:
	# Step treads are verified as geometry (tops monotonic, contiguous run,
	# rises within snap): physics rays stay for corridor/barrier (StaticBody).
	var tops: Array = []
	var spans: Array = []
	for si in range(5):
		var n := _find_node(b, "Sopana%d" % (si + 1))
		if n == null or not (n is CSGBox3D):
			_errs.append("Sopana%d missing" % (si + 1))
			return
		var box := n as CSGBox3D
		var top: float = (box as Node3D).position.y + box.size.y / 2.0
		tops.append(top)
		spans.append([(box as Node3D).position.x - box.size.x / 2.0, (box as Node3D).position.x + box.size.x / 2.0])
	for si in range(5):
		if absf(float(tops[si]) - (0.2 + float(si) * 0.2)) > 0.01:
			_errs.append("Sopana%d top %.2f, want %.2f" % [si + 1, float(tops[si]), 0.2 + float(si) * 0.2])
	for si in range(4):
		if float(spans[si][0]) > float(spans[si + 1][1]) + 0.05:
			_errs.append("sopana run gap between steps %d/%d" % [si + 1, si + 2])
	if float(spans[4][0]) > 2.6:
		_errs.append("top step west edge %.2f misses adhishthana" % float(spans[4][0]))
	var ramp := _find_node(b, "SopanaRamp")
	if ramp == null:
		_errs.append("SopanaRamp missing")
		return
	if not bool((ramp as CSGBox3D).use_collision):
		_errs.append("SopanaRamp must collide")
	if absf((ramp as Node3D).rotation.z) > 0.785:
		_errs.append("SopanaRamp slope %.2f exceeds walkable 45deg" % absf((ramp as Node3D).rotation.z))

func _ready() -> void:
	var b = Node3D.new()
	b.set_script(Builder)
	add_child(b)
	if not b.build_from("res://spec.json"):
		push_error("BUILD FAIL: " + str(b.errors))
		get_tree().quit(1)
		return
	# Test-only walkable ground (kalari ksetra.tscn owns the real 70m Ground).
	var ground := StaticBody3D.new()
	ground.name = "TestGround"
	var gcol := CollisionShape3D.new()
	var gshape := BoxShape3D.new()
	gshape.size = Vector3(70, 0.2, 70)
	gcol.shape = gshape
	ground.position = Vector3(0, -0.1, 0)
	ground.add_child(gcol)
	add_child(ground)
	# CSG collision bodies register a few frames after build; settle first.
	for i in range(8):
		await get_tree().physics_frame
	# Walkable floor along the route (ground-backed waypoints).
	_floor(28.0, 0.0, 0.0, "spawn outside maryada")
	_floor(22.0, 0.0, 0.0, "sivelipura court")
	_floor(16.0, 0.0, 0.0, "vilakkumadam court")
	_floor(13.32, 1.0, 0.0, "gopura passage")
	_floor(10.0, 2.0, 0.0, "courtyard")
	# Sanctum climb verified as step geometry + walk ramp (see _check_sopana).
	_check_sopana(b)
	# Open gates (short rays through each wall line, expect empty).
	_ray(Vector3(27.6, 1, 0), Vector3(25.6, 1, 0), "maryada gate", false)
	_ray(Vector3(19.6, 1, 0), Vector3(17.6, 1, 0), "vilakku gate", false)
	_ray(Vector3(15.6, 1, 0), Vector3(14.0, 1, 0), "nalambalam gate", false)
	_ray(Vector3(14.5, 1, 1.0), Vector3(12.5, 1, 1.0), "gopura passage", false)
	# Sanctum barrier holds at the door gap.
	var hit := _ray(Vector3(4.5, 2, 0), Vector3(1.5, 2, 0), "sanctum barrier", true, "SanctumBarrier")
	if not hit.is_empty():
		var hx: float = (hit.get("position") as Vector3).x
		if hx < 1.9 or hx > 2.5:
			_errs.append("barrier at x=%.2f, want 1.9..2.5" % hx)
	if _errs.is_empty():
		print("TRAVERSE OK: gopura->courtyard->mandapa walkable, barrier holds at door")
		get_tree().quit(0)
	else:
		for e in _errs:
			push_error(e)
		get_tree().quit(1)
