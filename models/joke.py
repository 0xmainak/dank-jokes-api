from pydantic import BaseModel
from typing import Optional


class JokeResponse(BaseModel):
    joke: str
    author: str
    category: str
    language: str


class MessageResponse(BaseModel):
    message: str

class CountResponse(BaseModel):
    total: int
    hindi: int
    english: int