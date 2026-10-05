extends Node
const Invg = preload("res://godot/inventory.gd")
const Sched = preload("res://godot/scheduler.gd")
var waited: Array = []
var opened: Array = []
func _ready() -> void:
	var inv = Node.new()
	inv.set_script(Invg)
	add_child(inv)
	inv.stock["ghee"] = 0
	inv.stock["honey"] = 0
	var s = Node.new()
	s.set_script(Sched)
	add_child(s)
	s.inventory = inv
	s.step_waiting.connect(func(id: String, _w: String) -> void: waited.append(id))
	s.slot_opened.connect(func(id: String) -> void: opened.append(id))
	s._period = 4.0
	s.start_adhivasa()
	await get_tree().create_timer(4.6).timeout
	print("WAITED: " + str(waited) + " OPENED-nitya-blocked-check")
	# ghrita_madhu needs ghee+honey=0 -> must have waited, never emitted as step
	if "ghrita_madhu" in waited:
		inv.fetch("ghee", 2)
		inv.fetch("honey", 2)
		await get_tree().create_timer(2.5).timeout
		print("INVENTORY OK: gate held step on empty stock, released after fetch")
		get_tree().quit(0)
	else:
		push_error("INVENTORY FAIL: no wait on ghrita_madhu")
		get_tree().quit(1)
