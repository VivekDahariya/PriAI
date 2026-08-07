from sentence_transformers import SentenceTransformer

from app.storage.chroma import ChromaVectorStore
from app.storage.models import KnowledgeChunk

# Load embedding model
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Initialize storage
store = ChromaVectorStore("test_collection")

# Clear old test data (optional but recommended while testing)
try:
    store.delete()
except:
    pass

store = ChromaVectorStore("test_collection")

# Store a document
text = "PriAI is an offline AI platform."

embedding = model.encode(text)

chunk = KnowledgeChunk(
    id="1",
    text=text,
    source="demo",
    chunk_index=0,
    embedding=embedding.tolist()
)

store.add([chunk])

print("✅ Knowledge Stored Successfully!")

# -----------------------------
# TEST RETRIEVAL
# -----------------------------

query = "What is PriAI?"

query_embedding = model.encode(query)

results = store.search(
    query_embedding=query_embedding.tolist(),
    top_k=1
)

print("\n🔍 Search Results:\n")

print(results[0]["text"])