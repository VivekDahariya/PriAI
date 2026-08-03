from app.compiler.models import (
    CompiledKnowledge,
    KnowledgeUnit,
    MetadataDictionary
)

from app.compiler.relation_builder import RelationBuilder

from app.hkr.manager import HKRManager
from app.hkr.dictionary import KnowledgeDictionary


class KnowledgeCompiler:

    def __init__(self):

        self.hkr = HKRManager()

        self.dictionary = KnowledgeDictionary()

        self.relation_builder = RelationBuilder()

    def compile(
        self,
        document_name: str,
        chunks: list[str]
    ):

        document = self.hkr.create_document(
            document_name
        )

        units = []

        for i, chunk in enumerate(chunks):

            page = self.hkr.add_child(

                parent_id=document.root_node,

                level="page",

                metadata={
                    "page": i + 1
                }

            )

            units.append(

                KnowledgeUnit(

                    id=f"KU{i + 1}",

                    text=chunk,

                    hkr_node_id=page.id,

                    metadata=self.dictionary.encode_metadata(
                        {
                            "document": document_name,
                            "page": i + 1
                        }
                    )

                )

            )

        relations = self.relation_builder.build(
            units
        )

        compiled = CompiledKnowledge(

            document=document,

            hierarchy=self.hkr.nodes,

            dictionary=MetadataDictionary(

                word_to_id=self.dictionary.word_to_id,

                id_to_word=self.dictionary.id_to_word

            ),

            units=units,

            relations=relations

        )

        return compiled