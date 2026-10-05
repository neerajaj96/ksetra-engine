extends Node
const Sched = preload("res://godot/scheduler.gd")
var steps: Array = []
func _ready() -> void:
	var s = Node.new()
	s.set_script(Sched)
	add_child(s)
	s.rite_stepped.connect(func(id: String) -> void: steps.append(id))
	s._period = 4.0
	s.start_homa_prelude()
	await get_tree().create_timer(5.0).timeout
	print("HOMA STEPS: " + str(steps))
	if steps == ["kunda_shosha", "pitha_shakti", "agni_adhana", "ghee_archana"]:
		print("HOMA OK: SESHA prelude runs in verse order")
		get_tree().quit(0)
	else:
		push_error("HOMA FAIL")
		get_tree().quit(1)
