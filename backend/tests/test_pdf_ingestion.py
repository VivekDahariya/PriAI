from app.ingestion.loader import load_document


pdf_path = "sample.pdf"

text = load_document(pdf_path)

print("\n--- Extracted Text Preview ---\n")

print(text[:1000])