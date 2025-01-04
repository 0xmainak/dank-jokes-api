# Jokes API 🎭

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

A simple and fun API that serves jokes in different languages, built with FastAPI and MongoDB.

## 🚀 Features

- Get random jokes in Hindi
- Clean and simple API endpoints
- Beautiful documentation page
- MongoDB integration for data storage

## 🛠️ Tech Stack

- FastAPI - Modern Python web framework
- MongoDB - NoSQL database
- Python 3.x - Programming language
- Uvicorn - ASGI web server

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/docs` | GET | API documentation |
| `/random/hindi` | GET | Get a random Hindi joke |

Visit the [API Documentation](http://104.197.122.48:6901/docs) for detailed information about using the endpoints.

## 🏃‍♂️ Running Locally

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pymongo python-dotenv
   ```
3. Create a `.env` file with your MongoDB connection string:
   ```
   MONGO=your_mongodb_connection_string
   ```
4. Run the server:
   ```bash
   python main.py
   ```