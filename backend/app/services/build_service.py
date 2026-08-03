from sentence_transformers import SentenceTransformer

from app.ingestion.loader import load_document
from app.processing.pipeline import process_document
from app.storage.chroma import ChromaVectorStore
from app.storage.models import KnowledgeChunk
from app.utils.slug import generate_ai_id
from app.registry.manager import RegistryManager
from app.compiler.compiler import KnowledgeCompiler


from app.registry.manager import RegistryManager
from app.compiler.compiler import KnowledgeCompiler
from app.compiler.relation_store import RelationStore

class BuildService:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.registry = RegistryManager()
        self.relation_store = RelationStore()
        self.compiler = KnowledgeCompiler()


    def build(self, ai_name: str, files: list[str]):

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
            
            self.relation_store.save(
                ai_id,
                compiled.relations
            )

            print(f"📦 {len(compiled.units)} chunks created")

            knowledge_chunks = []

            for unit in compiled.units:

                embedding = self.embedding_model.encode(
                    unit.text
                )

                knowledge_chunks.append(

                    KnowledgeChunk(

                        id=f"{ai_id}_{unit.id}",

                        text=unit.text,

                        source=pdf_path,

                        chunk_index=unit.metadata["page"] - 1,

                        embedding=embedding.tolist(),

                        hkr_node_id=unit.hkr_node_id

                    )

                )

            print("💾 Storing...")

            store.add(knowledge_chunks)

            total_chunks += len(knowledge_chunks)

        # -----------------------------
        # Dynamic Knowledge Metadata
        # -----------------------------

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

        # -----------------------------
        # Registry Update
        # -----------------------------

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


