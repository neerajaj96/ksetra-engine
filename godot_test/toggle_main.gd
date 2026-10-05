extends Node
# Toggle proof: demo builds slice 0 then slice 1, both provenance-closed.
const Demo = preload("res://godot/ksetra_demo.gd")

func _ready() -> void:
	var d = Node3D.new()
	d.set_script(Demo)
	add_child(d)
	await get_tree().process_frame
	var c0 := _count(d)
	d._build_slice(1)
	await get_tree().process_frame
	await get_tree().process_frame
	var c1 := _count(d)
	print("TOGGLE: slice0 nodes=%d slice1 nodes=%d" % [c0, c1])
	if c0 > 50 and c1 > 50:
		print("TOGGLE OK: both slices build + switch live")
		get_tree().quit(0)
	else:
		push_error("TOGGLE FAIL")
		get_tree().quit(1)

var _n := 0

func _count(d: Node) -> int:
	_n = 0
	_recurse(d)
	return _n

func _recurse(x: Node) -> void:
	if x.has_meta("provenance"):
		_n += 1
	for c in x.get_children():
		_recurse(c)
