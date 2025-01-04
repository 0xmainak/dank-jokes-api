from os import getenv
from fastapi import FastAPI, HTTPException, Request
import uvicorn
from pymongo import MongoClient
from dotenv import load_dotenv
import random
from fastapi.responses import HTMLResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
from typing import Optional

class JokeResponse(BaseModel):
    joke: str
    author: str 
    category: str
    language: str

class MessageResponse(BaseModel):
    message: str

load_dotenv()
db = MongoClient(getenv("MONGO"))

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(docs_url=None, redoc_url=None)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

def format_data(data) -> JokeResponse:
    return JokeResponse(
        joke=data["joke"],
        author=data["author"],
        category=data["category"],
        language=data["language"]
    )

@app.get("/", response_model=MessageResponse)
# @limiter.limit("10/minute") 
def read_root(request: Request):
    return MessageResponse(message="Hello, World!")

@app.get("/docs")
# @limiter.limit("10/minute")
def get_docs(request: Request):
    return HTMLResponse(open("docs.html", "r").read())

@app.get("/random/hindi", response_model=JokeResponse)
@limiter.limit("30/minute")
def read_random_hindi(request: Request):
    data = db.jokes_db.jokes.find({"language": "Hindi"}).to_list()
    data = random.choice(data)
    return format_data(data)

if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port = 6901, reload=True)
