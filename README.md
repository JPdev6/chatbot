# Chatbot - Multi-Model Conversational AI with Flask

A ChatGPT-like chatbot built with Flask, supporting **rule-based responses**, **machine learning conversation models**, and **transformer-based dialogue systems**.
Persistent chat history, sentiment analysis, and FAQ analytics are included.
Easily deployable with **Docker** or on traditional platforms like **Render**.

---

## ✨ Features

- 🐩 **Three Chatbot Modes**:
  - **Rule-Based Chatbot** (simple if-else logic)
  - **Machine Learning Chatbot** (using scikit-learn models)
  - **Transformer-Based Chatbot** (using HuggingFace Transformers)
- 💬 Room-specific conversations
- 🧠 Persistent chat history with MongoDB
- 📊 Sentiment analysis for each message (TextBlob)
- 🚀 Analytics for most frequently asked questions
- 🚨 Real-time communication with Flask-SocketIO
- 🚧 **Dockerized** for seamless deployment

---

## 💡 Technology Stack

- **Backend**: Flask, Flask-SocketIO
- **Database**: MongoDB
- **NLP**: TextBlob, scikit-learn, Transformers (HuggingFace)
- **Deployment**: Render / Docker

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/JPdev6/chatbot.git
cd chatbot
```

### 2. Set up the environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run locally

```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

---

## 🚧 Docker Deployment (Optional)

You can run the entire chatbot inside a Docker container:

```bash
docker build -t chatbot .
docker run -p 5000:5000 chatbot
```

Or use **docker-compose** to spin up with MongoDB:

```bash
docker-compose up --build
```

---

## 👀 Live Demo

Easily deployable on **Render**:
- Configure `gunicorn` as the start command: `gunicorn app:app`
- Use the provided `Procfile` and `requirements.txt`.

---

## 💪 Contributions

Contributions, issues, and feature requests are welcome!

---

## © License

This project is licensed under the MIT License.
