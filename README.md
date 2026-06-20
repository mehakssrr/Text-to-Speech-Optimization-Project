Text-to-Speech (TTS) Optimization Project
Overview
This project converts text into speech using Python, FastAPI, and gTTS. The main objective is to generate audio output from user-provided text while improving response time and supporting audio streaming.

Features
Convert text to speech
Generate MP3 audio files
FastAPI-based API
Audio streaming support
Simple and lightweight implementation
Technologies Used
Python
FastAPI
gTTS (Google Text-to-Speech)
Uvicorn
Project Structure
tts_project/

├── main.py

├── test.py

├── requirements.txt

├── audio/

└── README.md

Installation
Clone the repository: git clone https://github.com/divya5055/TTS-Project.git

Navigate to the project folder: cd TTS-Project

Install dependencies: pip install -r requirements.txt

Running the Project
Start the FastAPI server:

uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000

API Endpoint
Generate speech:

http://127.0.0.1:8000/tts?text=Hello World

Output
MP3 audio file
Audio stream response
Future Improvements
Real-time streaming
Multiple language support
Voice selection
Improved speech quality
