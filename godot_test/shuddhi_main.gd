extends Node
const Sched = preload("res://godot/scheduler.gd")
var steps: Array = []
func _ready() -> void:
	var s = Node.new()
	s.set_script(Sched)
	add_child(s)
	s.rite_stepped.connect(func(id: String) -> void: steps.append(id))
	s._period = 4.0
	s.start_shuddhi()
	await get_tree().create_timer(3.0).timeout
	print("SHUDDHI STEPS: " + str(steps))
	if steps == ["dig_bandha", "nadi_shuddhi"]:
		print("SHUDDHI OK: SESHA P8 program runs in verse order")
		get_tree().quit(0)
	else:
		push_error("SHUDDHI FAIL")
		get_tree().quit(1)
