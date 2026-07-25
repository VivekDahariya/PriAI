from fastapi import FastAPI

app = FastAPI(
    title="PriAI Backend"
)

@app.get("/")
def home():
    return {
        "message": "PriAI Engine Running"
    }