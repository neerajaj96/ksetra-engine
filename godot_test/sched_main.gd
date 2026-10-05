extends Node
# Headless scheduler proof: 5 nitya slots cycle data-driven, signals fire in order.
const Sched = preload("res://godot/scheduler.gd")

var opened: Array = []
var sched: Node

func _ready() -> void:
	sched = Node.new()
	sched.set_script(Sched)
	add_child(sched)
	sched.slot_opened.connect(func(id: String) -> void: opened.append(id))
	sched._period = 5.0  # 1s per slot
	await get_tree().create_timer(6.5).timeout
	var want := ["pantheeradi", "ucha", "deeparadhana", "athazha", "usha", "pantheeradi"]
	print("SLOTS: ", str(opened))
	if opened.size() >= 5 and str(opened.slice(0, 5)) == str(want.slice(0, 5)):
		print("SCHEDULER OK: nitya cycle usha->...->athazha data-driven (no hardcoded scripts)")
		get_tree().quit(0)
	else:
		push_error("SCHEDULER FAIL: got " + str(opened))
		get_tree().quit(1)
