from app.ingestion.loader import load_document
from app.processing.pipeline import process_document

pdf_path = "sample.pdf"

print("\n📄 Loading PDF...")
text = load_document(pdf_path)

print("✅ PDF Loaded")

print("\n🧹 Cleaning & Chunking...")
chunks = process_document(text)

print(f"\n✅ Total Chunks Created: {len(chunks)}")

if chunks:
    print("\n📦 First Chunk Preview:\n")
    print(chunks[0])
    print(f"\n📏 First Chunk Length: {len(chunks[0])} characters")