from sentence_transformers import SentenceTransformer

from app.storage.chroma import ChromaVectorStore

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

store = ChromaVectorStore(
    "computer_science"
)

embedding = model.encode(
    "What are neural networks?"
).tolist()

results = store.search(
    embedding,
    top_k=3
)

for r in results:

    print(r)