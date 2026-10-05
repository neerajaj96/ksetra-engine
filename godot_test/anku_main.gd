extends Node
const Sched = preload("res://godot/scheduler.gd")
var steps: Array = []
func _ready() -> void:
	var s = Node.new()
	s.set_script(Sched)
	add_child(s)
	s.rite_stepped.connect(func(id: String) -> void: steps.append(id))
	s._period = 4.0
	s.start_ankurarpana()
	await get_tree().create_timer(3.0).timeout
	print("ANKU STEPS: " + str(steps))
	if steps == ["palika_place", "bija_sow"]:
		print("ANKURARPANA OK: P3 program runs in verse order")
		get_tree().quit(0)
	else:
		push_error("ANKURARPANA FAIL")
		get_tree().quit(1)
