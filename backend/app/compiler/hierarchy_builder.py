from .hierarchy_models import KnowledgeHierarchyNode



class HierarchyBuilder:


    def build(
        self,
        document_name,
        units
    ):


        nodes = {}



        document = KnowledgeHierarchyNode(

            name=document_name,

            node_type="document"

        )


        nodes[document.id] = document



        pages = {}



        for unit in units:


            page_id = unit.parent_id



            if page_id not in pages:


                page_node = KnowledgeHierarchyNode(

                    id=page_id,

                    name=f"Page {unit.metadata.get('page')}",

                    node_type="page",

                    parent_id=document.id

                )


                pages[page_id] = page_node


                nodes[page_node.id] = page_node


                document.children.append(
                    page_node.id
                )



            chunk_node = KnowledgeHierarchyNode(

                id=unit.hkr_node_id,

                name=f"Chunk {unit.id}",

                node_type="chunk",

                parent_id=page_id,

                metadata={

                    "text": unit.text,

                    "hkr_node_id": unit.hkr_node_id

                }

            )


            nodes[chunk_node.id] = chunk_node



            pages[page_id].children.append(
                chunk_node.id
            )



        return nodes