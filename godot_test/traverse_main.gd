extends Node3D
# Traverse proof: the east axis is walkable from outside Maryada to the
# sanctum door, where SanctumBarrier (K-TANTRI-ONLY) holds. No player needed:
# physics rays walk the route a devotee would take.
const Builder = preload("res://godot/ksetra_builder.gd")

var _errs: Array = []

func _ray(from: Vector3, to: Vector3, label: String, expect_hit: bool, want_name := "", exclude: Array = []) -> Dictionary:
	var q := PhysicsRayQueryParameters3D.create(from, to)
	q.exclude = exclude
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
	# Tread plates ride the walk ramp (tops follow the 24deg slope +0.045, so
	# no riser walls the climb): assert monotonic run, even spacing, and that
	# the run meets the adhishthana. Ramp physics asserted below.
	var tops: Array = []
	var xs: Array = []
	for si in range(5):
		var n := _find_node(b, "SopanaTread_%d" % (si + 1))
		if n == null or not (n is MeshInstance3D):
			_errs.append("SopanaTread_%d missing" % (si + 1))
			return
		var mi := n as MeshInstance3D
		tops.append((mi as Node3D).position.y + 0.03)
		xs.append((mi as Node3D).position.x)
	for si in range(5):
		if si > 0 and float(tops[si]) <= float(tops[si - 1]):
			_errs.append("treads not rising at %d" % (si + 1))
	for si in range(4):
		var d := float(tops[si + 1]) - float(tops[si])
		if d < 0.1 or d > 0.25:
			_errs.append("tread rise %.2f out of [0.1,0.25]" % d)
		if absf(float(xs[si]) - float(xs[si + 1]) - 0.4) > 0.01:
			_errs.append("tread spacing off at %d" % (si + 1))
	if float(tops[4]) < 0.9 or float(tops[4]) > 1.05:
		_errs.append("top tread %.2f misses adhishthana 1.08" % float(tops[4]))
	if float(xs[4]) > 2.8:
		_errs.append("top tread west edge misses adhishthana")
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
	# Auxiliary spaces: kulam curb step, kavu grove floor (outside the ring
	# wall), hall plinths (geometry: roofs overhead defeat downward rays).
	_floor(-13.3, 10.15, 0.2, "kulam north curb")
	_floor(-16.5, -13.0, 0.0, "kavu grove floor")
	_floor(6.32, -4.2, 0.0, "thidappalli fetch apron")
	var japa := _find_node(b, "JapaMandapa_Plinth")
	if japa == null or not (japa is CSGBox3D):
		_errs.append("JapaMandapa_Plinth missing")
	elif absf((japa as Node3D).position.y + (japa as CSGBox3D).size.y / 2.0 - 0.4) > 0.01:
		_errs.append("japa plinth top != 0.4")
	for mmi in ["PalikaSet", "BrahmaKalashaSet", "ParitaFlagSet", "KavuTrunkSet", "KavuCrownSet", "KavuCrownTopSet"]:
		if _find_node(b, mmi) == null:
			_errs.append("instanced set missing: " + mmi)
	# Pradakshina ring floor samples (between the 8 bali stones, r = uh + 2.5).
	for bi in range(8):
		var bang := TAU * float(bi) / 8.0
		_floor(cos(bang) * 11.14, sin(bang) * 11.14, 0.0, "pradakshina %d" % bi)
	# Open gates (short rays through each wall line, expect empty).
	_ray(Vector3(27.6, 1, 0), Vector3(25.6, 1, 0), "maryada gate", false)
	_ray(Vector3(19.6, 1, 0), Vector3(17.6, 1, 0), "vilakku gate", false)
	_ray(Vector3(15.6, 1, 0), Vector3(14.0, 1, 0), "nalambalam gate", false)
	_ray(Vector3(14.5, 1, 1.0), Vector3(12.5, 1, 1.0), "gopura passage", false)
	# Scripted capsule walker: real move_and_slide traversal down the east axis.
	# Same body spec as the fighter (r0.4/h1.8, snap 0.3); ends pressed against
	# the sanctum barrier, proving both walkability AND permission hold.
	var walker := CharacterBody3D.new()
	walker.name = "ProveWalker"
	var wcol := CollisionShape3D.new()
	var wcap := CapsuleShape3D.new()
	wcap.radius = 0.4
	wcap.height = 1.8
	wcol.shape = wcap
	wcol.position = Vector3(0, 0.9, 0)
	walker.add_child(wcol)
	walker.floor_snap_length = 0.3
	walker.position = Vector3(28, 1.0, 0)
	add_child(walker)
	var legs := [Vector3(20, 0, 0), Vector3(14.5, 0, 1.0), Vector3(12.0, 0, 1.0),
		Vector3(11.0, 0, 2.5), Vector3(10.0, 0, 2.0), Vector3(9.0, 0, 2.0),
		Vector3(5.0, 0, 2.0), Vector3(4.9, 0, 0.1), Vector3(3.6, 0, 0.1),
		Vector3(1.0, 0, 0)]
	var vy := 0.0
	for leg in legs:
		var target: Vector3 = leg
		var t := 0.0
		while t < 10.0:
			await get_tree().physics_frame
			t += get_physics_process_delta_time()
			var to := target - walker.position
			to.y = 0.0
			if to.length() < 0.6:
				break
			var dir := to.normalized()
			vy -= 9.8 * get_physics_process_delta_time()
			if walker.is_on_floor():
				vy = -0.5
			walker.velocity = Vector3(dir.x * 3.0, vy, dir.z * 3.0)
			walker.move_and_slide()
	if walker.position.x > 3.2 or walker.position.x < 1.85:
		_errs.append("walker holds at x=%.2f, want pressed at barrier 1.85..3.2" % walker.position.x)
	# Sanctum barrier holds at the door gap (ray proof alongside the walker;
	# walker excluded so its own capsule never shadows the barrier).
	var hit := _ray(Vector3(4.5, 2, 0), Vector3(1.5, 2, 0), "sanctum barrier", true, "SanctumBarrier", [walker.get_rid()])
	if not hit.is_empty():
		var hx: float = (hit["position"] as Vector3).x
		if hx < 1.9 or hx > 2.5:
			_errs.append("barrier at x=%.2f, want 1.9..2.5" % hx)
	# Circular-slice smoke: west branch builds, door frame + linga present.
	var b2 = Node3D.new()
	b2.set_script(Builder)
	add_child(b2)
	if not b2.build_from("res://spec2.json"):
		_errs.append("circular BUILD FAIL: " + str(b2.errors))
	else:
		for cn in ["DoorFrame", "LingaBrahma", "GopuraJambL", "ConeRafterSet", "ConeDressSet"]:
			if _find_node(b2, cn) == null:
				_errs.append("circular node missing: " + cn)
	if _errs.is_empty():
		print("TRAVERSE OK: gopura->courtyard->mandapa walkable, barrier holds at door")
		get_tree().quit(0)
	else:
		for e in _errs:
			push_error(e)
		get_tree().quit(1)
