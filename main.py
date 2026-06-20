import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from gtts import gTTS
from fastapi import FastAPI
from gtts import gTTS
import time
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("audio", exist_ok=True)

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "TTS API Running"}


@app.get("/tts")
def text_to_speech(text: str):

    if not text.strip():
        return {"error": "Text cannot be empty"}

    if len(text) > 500:
        return {"error": "Text too long. Maximum 500 characters allowed"}

    start = time.time()

    tts = gTTS(text=text, lang='en')
    file_path = "audio/output.mp3"
    tts.save(file_path)

    end = time.time()

    print("Latency:", round(end - start, 2), "seconds")

    return FileResponse(
        file_path,
        media_type="audio/mpeg",
        filename="output.mp3"
    )

@app.post("/tts")
def text_to_speech(data: TextInput):
    tts = gTTS(text=data.text, lang="en")

    file_path = "audio/output.mp3"
    tts.save(file_path)

    return FileResponse(
        file_path,
        media_type="audio/mpeg",
        filename="speech.mp3"
    )
@app.get("/stream")
def stream_audio():

    def generate():
        with open("audio/output.mp3", "rb") as audio:
            while chunk := audio.read(1024):
                yield chunk

    return StreamingResponse(
        generate(),
        media_type="audio/mpeg"
    )    
