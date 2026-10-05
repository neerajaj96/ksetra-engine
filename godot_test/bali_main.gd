extends Node
const Sched = preload("res://godot/scheduler.gd")
var steps: Array = []
func _ready() -> void:
	var s = Node.new()
	s.set_script(Sched)
	add_child(s)
	s.rite_stepped.connect(func(id: String) -> void: steps.append(id))
	s._period = 4.0
	s.start_bali_circuit()
	await get_tree().create_timer(4.0).timeout
	print("BALI STEPS: " + str(steps))
	if steps == ["savana_bali", "dvara_bali", "kshetrapala_bali"]:
		print("BALI OK: SESHA P5 circuit runs in verse order")
		get_tree().quit(0)
	else:
		push_error("BALI FAIL")
		get_tree().quit(1)
