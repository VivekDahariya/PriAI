from app.generation.prompt_builder import PromptBuilder

contexts = [

    {
        "text": "PriAI is an offline AI platform."
    },

    {
        "text": "It builds AI assistants from user knowledge."
    }

]

builder = PromptBuilder()

prompt = builder.build(

    question="What is PriAI?",

    contexts=contexts

)

print(prompt)