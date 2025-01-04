from os import getenv
from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
from dotenv import load_dotenv
import random


load_dotenv()
db = MongoClient(getenv("MONGO"))

app = FastAPI()
def format_data(data):
    return {
        "joke": data["joke"],
        "author": data["author"],
        "category": data["category"],
        "language": data["language"]
    }
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/random/hindi")
def read_random_hindi():
    data = db.jokes_db.jokes.find({"language": "Hindi"}).to_list()
    data = random.choice(data)
    return format_data(data)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

