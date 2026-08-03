from app.compiler.models import (
    KnowledgeUnit,
    KnowledgeRelation,
)
from app.compiler.relation_builder import RelationBuilder

units = [

    KnowledgeUnit(
        id="KU1",
        text="Neural Networks",
        hkr_node_id="N1",
        metadata={}
    ),

    KnowledgeUnit(
        id="KU2",
        text="Gradient Descent",
        hkr_node_id="N2",
        metadata={}
    ),

    KnowledgeUnit(
        id="KU3",
        text="Loss Function",
        hkr_node_id="N3",
        metadata={}
    )

]

builder = RelationBuilder()

relations = builder.build(units)

for r in relations:

    print(r)