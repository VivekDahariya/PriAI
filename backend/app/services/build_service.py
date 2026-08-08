import hashlib

from sentence_transformers import SentenceTransformer

from app.compiler.concept_relation_store import ConceptRelationStore
from app.compiler.compiler import KnowledgeCompiler
from app.compiler.concept_store import ConceptStore
from app.compiler.models import ConceptNode
from app.compiler.relation_store import RelationStore

from app.ingestion.loader import load_document
from app.processing.pipeline import process_document

from app.registry.manager import RegistryManager

from app.storage.chroma import ChromaVectorStore
from app.storage.models import KnowledgeChunk

from app.utils.slug import generate_ai_id


class BuildService:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.registry = RegistryManager()

        self.compiler = KnowledgeCompiler()

        self.relation_store = RelationStore()

        self.concept_store = ConceptStore()

        self.concept_relation_store = ConceptRelationStore()


    def build(
        self,
        ai_name: str,
        files: list[str]
    ):

        ai_id = generate_ai_id(ai_name)

        print(f"\n🤖 Building AI: {ai_name}")
        print(f"🆔 AI ID: {ai_id}")

        store = ChromaVectorStore(ai_id)

        total_chunks = 0


        for pdf_path in files:

            print(f"\n📄 Loading: {pdf_path}")

            text = load_document(pdf_path)

            print("🧹 Processing...")

            chunks = process_document(text)


            compiled = self.compiler.compile(

                document_name=ai_name,

                chunks=chunks

            )


            # ----------------------------------------
            # Save / Merge Concepts
            # ----------------------------------------

            existing = self.concept_store.load(
                ai_id
            )


            existing_map = {

                c["name"].lower(): c

                for c in existing

            }


            for concept in compiled.concepts:

                key = concept.name.lower()


                if key in existing_map:

                    existing_map[key]["chunk_ids"].extend(

                        concept.chunk_ids

                    )

                    existing_map[key]["chunk_ids"] = list(

                        dict.fromkeys(

                            existing_map[key]["chunk_ids"]

                        )

                    )


                else:

                    existing_map[key] = {

                        "id": concept.id,

                        "name": concept.name,

                        "chunk_ids": concept.chunk_ids

                    }


            merged_concepts = [

                ConceptNode(

                    id=value["id"],

                    name=value["name"],

                    chunk_ids=value["chunk_ids"]

                )

                for value in existing_map.values()

            ]


            self.concept_store.save(

                ai_id,

                merged_concepts

            )


            # ----------------------------------------
            # Save / Merge Normal Relations
            # ----------------------------------------

            existing_relations = self.relation_store.load(
                ai_id
            )


            relation_keys = {

                (
                    r.get("source") if isinstance(r, dict) else r.source,
                    r.get("target") if isinstance(r, dict) else r.target,
                    r.get("relation") if isinstance(r, dict) else r.relation
                )

                for r in existing_relations

            }


            for relation in compiled.relations:

                key = (

                    relation.source,

                    relation.target,

                    relation.relation

                )


                if key not in relation_keys:

                    existing_relations.append(
                        relation
                    )

                    relation_keys.add(
                        key
                    )


            self.relation_store.save(

                ai_id,

                existing_relations

            )


            # ----------------------------------------
            # Save / Merge Concept Relations
            # ----------------------------------------

            existing_concept_relations = self.concept_relation_store.load(

                ai_id

            )


            relation_keys = {

                (
                    r.source,

                    r.target,

                    r.relation

                )

                for r in existing_concept_relations

            }


            for relation in compiled.concept_relations:

                key = (

                    relation.source,

                    relation.target,

                    relation.relation

                )


                if key not in relation_keys:

                    existing_concept_relations.append(

                        relation

                    )

                    relation_keys.add(

                        key

                    )


            self.concept_relation_store.save(

                ai_id,

                existing_concept_relations

            )


            print(

                f"📦 {len(compiled.units)} chunks created"

            )


            knowledge_chunks = []


            for unit in compiled.units:


                embedding = self.embedding_model.encode(

                    unit.text

                )


                chunk_id = hashlib.md5(

                    f"{ai_id}_{pdf_path}_{unit.id}".encode()

                ).hexdigest()


                knowledge_chunks.append(

                    KnowledgeChunk(

                        id=chunk_id,

                        knowledge_unit_id=unit.id,

                        text=unit.text,

                        source=pdf_path,

                        chunk_index=unit.metadata["page"] - 1,

                        embedding=embedding.tolist(),

                        hkr_node_id=unit.hkr_node_id

                    )

                )


            print("💾 Storing...")


            store.add(

                knowledge_chunks

            )


            total_chunks += len(

                knowledge_chunks

            )


        # ----------------------------------------
        # Knowledge Density
        # ----------------------------------------

        if total_chunks < 100:

            density = "Low"

            suggested_top_k = 8

            suggested_threshold = 0.55


        elif total_chunks < 1000:

            density = "Medium"

            suggested_top_k = 6

            suggested_threshold = 0.70


        else:

            density = "High"

            suggested_top_k = 4

            suggested_threshold = 0.82



        # ----------------------------------------
        # Registry
        # ----------------------------------------

        self.registry.register(

            ai_id=ai_id,

            name=ai_name,

            documents=len(files),

            chunks=total_chunks,

            knowledge_density=density,

            suggested_top_k=suggested_top_k,

            suggested_threshold=suggested_threshold

        )


        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━")

        print("✅ AI Build Completed")

        print(f"AI Name      : {ai_name}")

        print(f"AI ID        : {ai_id}")

        print(f"Files        : {len(files)}")

        print(f"Total Chunks : {total_chunks}")

        print(f"Density      : {density}")

        print(f"Top-K        : {suggested_top_k}")

        print(f"Threshold    : {suggested_threshold}")

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━")