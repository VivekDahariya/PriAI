from app.services.retrieval_service import RetrievalService

service = RetrievalService()

results = service.retrieve(
    ai_id="Computer Science",
    question="What is PriAI?"
)

print()

for i, result in enumerate(results, 1):

    print(f"Result {i}")
    print("-" * 40)
    print(result["text"])
    print(result["source"])
    print()