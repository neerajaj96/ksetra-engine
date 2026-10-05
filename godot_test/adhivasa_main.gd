extends Node
const Sched = preload("res://godot/scheduler.gd")
var steps: Array = []
func _ready() -> void:
	var s = Node.new()
	s.set_script(Sched)
	add_child(s)
	s.rite_stepped.connect(func(id: String) -> void: steps.append(id))
	s._period = 4.0  # 1s per rite step
	print("first: " + s.start_adhivasa())
	await get_tree().create_timer(8.0).timeout
	print("STEPS: " + str(steps))
	if steps == ["kautuka_bandhana", "mandapa_shuddhi", "shayya_build", "deepa_light", "ghrita_madhu", "shayana"]:
		print("ADHIVASA OK: P4 program runs in verse order")
		get_tree().quit(0)
	else:
		push_error("ADHIVASA FAIL")
		get_tree().quit(1)
