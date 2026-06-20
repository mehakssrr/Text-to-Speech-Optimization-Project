# 🎙️ Text-to-Speech (TTS) Optimization Project

A fast and lightweight web application that converts text into spoken audio files. Built using **Python**, **FastAPI**, and **gTTS** (Google Text-to-Speech), this project features quick response times and supports audio streaming.

---

## ✨ Features

* **Text-to-Speech Conversion**: Instantly turns any user-provided text into speech.
* **MP3 Generation**: Automatically creates and saves high-quality MP3 audio files.
* **FastAPI Backend**: Built on a modern, high-performance API framework.
* **Audio Streaming**: Supports real-time audio playback streaming for faster load times.
* **Lightweight Design**: Clean code structure with minimal external dependencies.

---

## 🛠️ Technologies Used

* **[Python](https://python.org)** - Core programming language
* **[FastAPI](https://fastapi.tiangolo.com/)** - Modern web framework for building APIs
* **[gTTS](https://pypi.org)** - Google Text-to-Speech library
* **[Uvicorn](https://uvicorn.org)** - Lightning-fast ASGI server implementation

---

## 📂 Project Structure

```text
tts_project/
├── main.py            # Main application setup and API endpoints
├── test.py            # Unit testing script
├── requirements.txt   # Required Python libraries and dependencies
├── audio/             # Directory where generated MP3 files are saved
└── README.md          # Project documentation
```

---

## 🚀 Installation & Setup

Follow these simple steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd TTS-Project
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Server
Start the development server using Uvicorn:
```bash
uvicorn main:app --reload
```

---

## 📡 API Endpoint Usage

Once the server is running, open your web browser or an API client (like Postman) and use the following link layout:

* **Base URL**: `http://127.0.0.1:8000`
* **TTS Endpoint**: `/tts`

### Example Request:
```text
http://127.0.0
```

### Expected Output:
* An **MP3 audio file** is generated and saved in the `audio/` folder.
* An **Audio stream response** plays directly in your web browser.

---

## 🔮 Future Improvements

- [ ] Add real-time user streaming
- [ ] Implement multiple language support options
- [ ] Add custom voice selection toggles
- [ ] Integrate advanced speech synthesis models for improved audio quality

---


## 👤 Author & Contact

* **Name**: Mehak Sharma
* **Email**: mehak.ssrr@gmail.com
* **GitHub**: https://github.com/mehakssrr
