from app.services.chat_service import ChatService


chat = ChatService()


response = chat.ask(

    ai_id="computer_science",

    question="What programming languages are mentioned?"

)


print()

print("ANSWER")
print("-" * 50)

print(response["answer"])


print()

print("SOURCES")
print("-" * 50)


for source in response["sources"]:

    print(
        source["source"]
    )