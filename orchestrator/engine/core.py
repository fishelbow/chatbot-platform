# Example logic inside your Orchestrator
import requests

def process_voice_command(audio_data):
    # 1. Speech to Text
    # 'stt' is the name of the container in docker-compose
    text = requests.post("http://stt:8000/transcribe", files={"file": audio_data}).json()

    # 2. Get LLM Response
    response = requests.post("http://llm:8000/chat", json={"prompt": text}).json()

    # 3. Text to Speech
    audio_out = requests.post("http://tts:8000/synthesize", json={"text": response}).content
    
    return audio_out
