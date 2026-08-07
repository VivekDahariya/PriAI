from app.compiler.models import (
    CompiledKnowledge,
    KnowledgeUnit,
    MetadataDictionary
)

from app.compiler.relation_builder import RelationBuilder
from app.compiler.concept_builder import ConceptBuilder
from app.compiler.concept_relation_builder import ConceptRelationBuilder
from app.compiler.concept_extractor import ConceptExtractor

from app.hkr.manager import HKRManager
from app.hkr.dictionary import KnowledgeDictionary


class KnowledgeCompiler:

    def __init__(self):

        self.hkr = HKRManager()

        self.dictionary = KnowledgeDictionary()

        self.relation_builder = RelationBuilder()

        self.concept_builder = ConceptBuilder()

        self.extractor = ConceptExtractor()

        self.concept_relation_builder = ConceptRelationBuilder()

    def compile(

        self,

        document_name: str,

        chunks: list[str]

    ):

        document = self.hkr.create_document(
            document_name
        )

        units = []

        # reset concept index
        self.concept_builder = ConceptBuilder()

        for i, chunk in enumerate(chunks):

            page = self.hkr.add_child(

                parent_id=document.root_node,

                level="page",

                metadata={

                    "page": i + 1

                }

            )

            chunk_node = self.hkr.add_child(

                parent_id=page.id,

                level="chunk",

                metadata={

                    "page": i + 1,

                    "text": chunk

                }

            )

            encoded_metadata = self.dictionary.encode_metadata(

                {

                    "document": document_name,

                    "page": i + 1

                }

            )

            concepts = self.extractor.extract(

                chunk

            )

            unit = KnowledgeUnit(

                id=f"KU{i+1}",

                text=chunk,

                hkr_node_id=chunk_node.id,

                parent_id=page.id,

                level="chunk",

                metadata=encoded_metadata,

                concepts=concepts

            )

            units.append(

                unit

            )

            self.concept_builder.add_concepts(

                chunk_id=unit.id,

                concepts=unit.concepts

            )

        relations = self.relation_builder.build(

            units

        )

        concepts = self.concept_builder.build()

        concept_relations = self.concept_relation_builder.build(

            concepts,

            units

        )

        return CompiledKnowledge(

            document=document,

            hierarchy=self.hkr.nodes,

            dictionary=MetadataDictionary(

                word_to_id=self.dictionary.word_to_id,

                id_to_word=self.dictionary.id_to_word

            ),

            units=units,

            relations=relations,

            concepts=concepts,

            concept_relations=concept_relations

        )