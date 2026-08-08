import ollama


class Generator:


    def __init__(
        self,
        model: str = "qwen2.5:3b"
    ):

        self.model = model



    def generate(
        self,
        prompt: str
    ) -> str:


        response = ollama.chat(

            model=self.model,

            messages=[

                {
                    "role": "system",
                    "content": (
                        "You are a private knowledge assistant. "
                        "Answer using only the provided context."
                    )
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            options={

                "temperature": 0.2

            }

        )


        return response["message"]["content"]