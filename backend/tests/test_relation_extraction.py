from app.compiler.models import KnowledgeUnit
from app.compiler.relation_builder import RelationBuilder

units = [

    KnowledgeUnit(
        id="KU1",
        text="Neural Networks are trained using Gradient Descent.",
        hkr_node_id="N1"
    ),

    KnowledgeUnit(
        id="KU2",
        text="Gradient Descent optimizes Loss Function.",
        hkr_node_id="N2"
    ),

    KnowledgeUnit(
        id="KU3",
        text="CNN is a type of Neural Network.",
        hkr_node_id="N3"
    )

]

builder = RelationBuilder()

relations = builder.build(units)

for r in relations:
    print(r)