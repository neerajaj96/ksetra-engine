extends Node3D
# Playable Vishnu-dvitala demo: orbit/zoom camera, click any member for its
# OBJECT -> RULE -> SOURCE chain. Launched directly (no HUD/world changes).
# Provenance: TS-P2V1-measure (massing), TS-P2V2-yoni (pairing), TS-P3V1-material.

const Builder = preload("res://godot/ksetra_builder.gd")
const Sched = preload("res://godot/scheduler.gd")
const Prov = preload("res://godot/provenance_lookup.gd")

var _yaw := 0.6
var _pitch := 0.5
var _dist := 26.0
var _target := Vector3(0, 2.5, 0)
var _cam: Camera3D
var _label: Label
var _prov = RefCounted.new()
var _slices := ["res://data/ksetra_vishnu_dvitala.json", "res://data/ksetra_shiva_ekatala.json"]
var _slice_i := 0
var _built: Node3D = null

func _ready() -> void:
	_cam = get_node_or_null("Camera") as Camera3D
	_label = get_node_or_null("ProvenanceUI/ProvenanceLabel") as Label
	var sched := Node.new()
	sched.set_script(Sched)
	add_child(sched)
	_build_slice(0)
	print("KSETRA DEMO OK: built + scheduler + provenance index live")

func _build_slice(i: int) -> void:
	_slice_i = i
	if _built != null:
		_built.queue_free()
		_built = null
	var b := Node3D.new()
	b.set_script(Builder)
	add_child(b)
	if not b.build_from(_slices[_slice_i]):
		_say("BUILD FAIL: " + str(b.errors))
		return
	_built = b
	var f := FileAccess.open(_slices[_slice_i], FileAccess.READ)
	var spec: Dictionary = JSON.parse_string(f.get_as_text())
	_prov.set_script(Prov)
	if not _prov.load_index(spec, "res://data/ksetra_rules.json"):
		_say("Provenance index missing.")
		return
	var meta: Dictionary = spec.get("meta", {})
	_say(str(meta.get("name", "?")) + " (K = toggle slice. Drag orbit, wheel zoom, click member.)")

func _process(_delta: float) -> void:
	if _cam == null:
		return
	var off := Vector3(cos(_pitch) * cos(_yaw), sin(_pitch), cos(_pitch) * sin(_yaw)) * _dist
	_cam.global_position = _target + off
	_cam.look_at(_target)

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and (event as InputEventKey).pressed and not (event as InputEventKey).echo:
		if (event as InputEventKey).keycode == KEY_K:
			_build_slice((_slice_i + 1) % _slices.size())
			return
	if event is InputEventMouseMotion and (event as InputEventMouseMotion).button_mask & MOUSE_BUTTON_MASK_LEFT:
		_yaw -= (event as InputEventMouseMotion).relative.x * 0.008
		_pitch = clampf(_pitch + (event as InputEventMouseMotion).relative.y * 0.008, 0.15, 1.3)
	elif event is InputEventMouseButton:
		var mb := event as InputEventMouseButton
		if mb.button_index == MOUSE_BUTTON_WHEEL_UP and mb.pressed:
			_dist = clampf(_dist - 1.5, 8.0, 60.0)
		elif mb.button_index == MOUSE_BUTTON_WHEEL_DOWN and mb.pressed:
			_dist = clampf(_dist + 1.5, 8.0, 60.0)
		elif mb.button_index == MOUSE_BUTTON_LEFT and mb.pressed:
			_pick(mb.position)

func _pick(screen_xy: Vector2) -> void:
	if _cam == null:
		return
	var from := _cam.project_ray_origin(screen_xy)
	var to := from + _cam.project_ray_normal(screen_xy) * 120.0
	var q := PhysicsRayQueryParameters3D.create(from, to)
	var hit := get_world_3d().direct_space_state.intersect_ray(q)
	if hit.is_empty():
		return
	var n: Node = hit.get("collider")
	while n != null and not n.has_meta("provenance"):
		n = n.get_parent()
	if n == null:
		return
	var prov: Array = n.get_meta("provenance")
	_say(str(n.name) + ": " + _prov.chain_for(str(prov[0])))

func _say(msg: String) -> void:
	if _label:
		_label.text = msg
	print(msg)
