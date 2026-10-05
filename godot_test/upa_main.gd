extends Node
const Sched = preload("res://godot/scheduler.gd")
var steps: Array = []
func _ready() -> void:
	var s = Node.new()
	s.set_script(Sched)
	add_child(s)
	s.rite_stepped.connect(func(id: String) -> void: steps.append(id))
	s._period = 5.0
	s.start_upachara()
	await get_tree().create_timer(6.0).timeout
	print("UPA STEPS: " + str(steps))
	if steps == ["avahana", "padya_achamana", "gandha_ambara", "pushpa_dhupa_deepa", "gayatri_touch"]:
		print("UPACHARA OK: P4V101B program runs in verse order")
		get_tree().quit(0)
	else:
		push_error("UPACHARA FAIL")
		get_tree().quit(1)
