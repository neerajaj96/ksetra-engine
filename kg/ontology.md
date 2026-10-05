# KSETRA Ontology v0.1

Nodes: Text, Edition, Passage, Commentary, Concept, Deity, Structure, Object,
Material, Role, Place, SpaceRel, TempRel, Procedure, Rule, Exception, Provenance.
Edges: ATTESTS, COMMENTS, TRANSLATES, CONSTRAINS, REQUIRES, PRECEDES,
LOCATED_IN, FACES, MEASURES, MADE_OF, PERFORMED_BY, PERMITTED_BY,
FORBIDDEN_TO, EXCEPTION_TO, CONTRADICTS, ABSTRACTION_OF.

Rule record (one YAML per rule, kg/rules/*.yaml):
id, claim_sa/en, rule_type (measure/proportion/orientation/spatial/sequence/role/permission/timing/exception/purification/maintenance),
params, applicability, source {work, edition, patala, verse, passage_chars, commentary, translator},
layer (PRIMARY/COMMENTARY/TRANSLATION/OCR/INTERPRETATION/OBSERVED/INFERENCE/ABSTRACTION),
game_abstraction, status (gated/partial/SOURCE_REQUIRED), contradicts[].

Provenance chain required: GAME OBJECT -> RULE -> KNOWLEDGE ENTITY -> SOURCE.
Contradictions are nodes, never merged.
