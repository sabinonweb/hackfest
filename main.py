from fastapi import FastAPI
from models.request import ImageRequest
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image 
import os
from metadata.read_data import read_metadata
from env.environment import virtualenv
from genai_llm.llm import summarize, read_nsfw, router

load_dotenv()

virtualenv()
summarize()
read_metadata()

app = FastAPI()
app.include_router(router, prefix="/api")

print(os.getenv('OPENAI_API_KEY'))

@app.get("/")
async def read_route():
    return { "Welcome to the HackFest" };

@app.get("/item/{item_id}")
async def read_items(item_id):
    return { "item_id" : item_id }

@app.post("/image")
async def image_detection(image: ImageRequest):
    print(image.name_of_the_object, " at ", image.position);



