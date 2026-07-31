from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

print("Model Loaded!")

vector = model.encode("Hello PriAI!")

print(f"Embedding Dimension: {len(vector)}")
print(vector[:10])