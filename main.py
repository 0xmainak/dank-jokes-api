from os import getenv
from fastapi import FastAPI, Request
import uvicorn
from pymongo import MongoClient
from dotenv import load_dotenv
import random
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from models import MessageResponse, JokeResponse, CountResponse



load_dotenv()
db = MongoClient(getenv("MONGO"))

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


def format_data(data) -> JokeResponse:
    return JokeResponse(
        joke=data["joke"],
        author=data["author"],
        category=data["category"],
        language=data["language"],
    )


@app.get("/", response_model=MessageResponse)
def read_root(request: Request):
    return MessageResponse(message="Hello, World!")


@app.get("/docs")
def get_docs(request: Request):
    return HTMLResponse(open("docs.html", "r").read())


@app.get("/random", response_model=JokeResponse)
@limiter.limit("30/minute")
def read_random(request: Request):
    data = db.jokes_db.jokes.find().to_list()
    data = random.choice(data)
    return format_data(data)


@app.get("/random/hindi", response_model=JokeResponse)
@limiter.limit("30/minute")
def read_random_hindi(request: Request):
    data = db.jokes_db.jokes.find({"language": "Hinglish"}).to_list()
    data = random.choice(data)
    return format_data(data)


@app.get("/random/english", response_model=JokeResponse)
@limiter.limit("30/minute")
def read_random_english(request: Request):
    data = db.jokes_db.jokes.find({"language": "English"}).to_list()
    data = random.choice(data)
    return format_data(data)


@app.get("/count", response_model=CountResponse)
# @limiter.limit("1/minute") 
def read_count(request: Request):
    total = db.jokes_db.jokes.count_documents({})
    hindi = db.jokes_db.jokes.count_documents({"language": "Hinglish"})
    english = db.jokes_db.jokes.count_documents({"language": "English"})

    return CountResponse(total=total, hindi=hindi, english=english)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=6901, reload=True)
