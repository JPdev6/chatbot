# ChatGPT-like Chatbot
A conversational chatbot powered by Flask, MongoDB, and Docker. This project supports room-based chat functionality, persistent chat history, and analytics for frequently asked questions.

## Features
- **Room-Based Chat**: Create and interact with different chatrooms (e.g., General, Support, Random).
- **Chat History**: View persistent and session-based chat history.
- **Sentiment Analysis**: Analyze user messages for sentiment.
- **Analytics**: Retrieve the most frequently asked questions in a specific room.
- **Dockerized Deployment**: Easily deploy the application with Docker Compose.


## Installation

### Prerequisites
- Python 3.10+
- Docker & Docker Compose

### Clone the Repository
```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot

pip install -r requirements.txt

python app.py

## Docker Deployment

### Build and Run
1. Build the Docker containers:
   ```bash
   docker-compose up --build


Access the application at http://localhost:5000/chat-ui.


---

#### **g) API Endpoints**
Document the available API endpoints.

```markdown
## API Endpoints

- `POST /chat`: Send a message and get a bot response.
- `GET /history`: Retrieve chat history for a specific room.
- `GET /analytics/frequent`: Retrieve the most frequently asked questions in a specific room.


## Technologies Used
- **Python** (Flask)
- **MongoDB** (Database)
- **Docker** (Containerization)
- **HTML/CSS/JavaScript** (Frontend)
- **TextBlob** (Sentiment Analysis)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](LICENSE)


