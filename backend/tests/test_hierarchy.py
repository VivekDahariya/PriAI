from app.compiler.hierarchy_builder import HierarchyBuilder
from app.compiler.models import KnowledgeUnit



units = [

    KnowledgeUnit(
        id="KU1",
        text="Neural Networks",
        hkr_node_id="chunk1",
        parent_id="page1",
        metadata={
            "page":1
        }
    ),


    KnowledgeUnit(
        id="KU2",
        text="Gradient Descent",
        hkr_node_id="chunk2",
        parent_id="page2",
        metadata={
            "page":2
        }
    )

]



builder = HierarchyBuilder()


tree = builder.build(
    "Machine Learning",
    units
)



print("\nHIERARCHY")
print("----------------")


for key,node in tree.items():

    print(
        node.node_type,
        node.name,
        node.children
    )