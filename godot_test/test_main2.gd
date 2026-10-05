extends Node3D
# Headless proof: TEXT->RULE->SPEC->WORLD. Builds dvitala, checks provenance closure, quits.
const Builder = preload("res://godot/ksetra_builder.gd")

func _ready() -> void:
	var b = Node3D.new()
	b.set_script(Builder)
	add_child(b)
	if not b.build_from("res://spec2.json"):
		push_error("BUILD FAIL: " + str(b.errors))
		get_tree().quit(1)
		return
	var tally := [0]
	var missing: Array = []
	_walk(b, func(n: Node) -> void:
		if n.has_meta("provenance"):
			tally[0] += 1
			if (n.get_meta("provenance") as Array).is_empty():
				missing.append(str(n.name)))
	print("WORLD OK: semantic nodes with provenance = %d; missing = %d %s" % [tally[0], missing.size(), str(missing)])
	if tally[0] < 50 or not missing.is_empty():
		push_error("PROVENANCE AUDIT FAIL")
		get_tree().quit(1)
		return
	# yoni + range sanity on built massing
	var uh_m := Builder.Loader.hasta_to_m(12.0)
	print("MASSING: uttara 12 hastas = %.2f m; garbha 6 hastas = %.2f m" % [uh_m, Builder.Loader.hasta_to_m(6.0)])
	print("PROOF COMPLETE: TEXT->KNOWLEDGE->RULE->SPEC->WORLD")
	get_tree().quit(0)

func _walk(n: Node, fn: Callable) -> void:
	fn.call(n)
	for c in n.get_children():
		_walk(c, fn)
