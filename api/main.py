from fastapi import FastAPI

app = FastAPI(
    title="Chatbot Platform API",
    version="1.0.0",
    description="API layer for core-engine, tts, stt, pso-bot-client, chat"
)

@app.get("/")
def root():
    return {"status": "ok"}