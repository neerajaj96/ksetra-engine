extends Node
# Provenance proof: spec node -> rule -> source chain renders in-engine.
const Prov = preload("res://godot/provenance_lookup.gd")

func _ready() -> void:
	var f := FileAccess.open("res://spec.json", FileAccess.READ)
	var spec: Dictionary = JSON.parse_string(f.get_as_text())
	var pl = RefCounted.new()
	pl.set_script(Prov)
	if not pl.load_index(spec, "res://data/ksetra_rules.json"):
		push_error("PROV FAIL: rules json missing")
		get_tree().quit(1)
		return
	# every complex node id must resolve its first provenance rule
	var bad: Array = []
	for nd in (spec.get("complex", {}) as Dictionary).get("nodes", []):
		var prov: Array = nd.get("provenance", [])
		var line: String = pl.chain_for(str(prov[0]) if not prov.is_empty() else "?")
		if line.begins_with("No rule"):
			bad.append(str(nd.get("id")))
	print("PROV SAMPLE: " + pl.chain_for("TS-P2V1-measure"))
	print("PROV SAMPLE: " + pl.chain_for("TS-P2V2-yoni"))
	if not bad.is_empty():
		push_error("PROV FAIL: " + str(bad))
		get_tree().quit(1)
		return
	print("PROVENANCE OK: %d nodes resolve OBJECT->RULE->SOURCE" % (spec["complex"]["nodes"] as Array).size())
	get_tree().quit(0)
