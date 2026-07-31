from app.services.build_service import BuildService

builder = BuildService()

builder.build(
    ai_name="Computer Science",
    files=["sample.pdf"]
)