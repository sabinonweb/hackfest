from .config import genai_config
import PIL.Image
import requests
import json
from dotenv import load_dotenv
import os
from fastapi import APIRouter, UploadFile

router = APIRouter()

def summarize():
    print("Inside summarize")
    model = genai_config()

    pumpkin = PIL.Image.open("./lib/gun.jpg")
    response = model.generate_content(["Describe the potential threats that the following image can have if we post it on social media", pumpkin])
    print("Response Text: ", response)
    #
# def calculate_security_score(object_name):
#     match object_name:
#         case 
#
async def read_nsfw():
    print("Inside Read NSFW")
    load_dotenv();
    edenai_api_key = os.getenv("EDENAI_API_KEY")
    headers = {"Authorization" : f"Bearer {edenai_api_key}"}
    url = "https://api.edenai.run/v2/image/explicit_content"
    data = {"providers" : "google"}
    files = {'file' : open("./lib/lor.jpg", 'rb')}

    response = requests.post(url, data=data, files=files, headers=headers)

    result = json.loads(response.text)
    print("NSFW Data: ", result)

@router.get("/test_nsfw")
async def test_nsfw():
    nsfw = await read_nsfw();
    return nsfw
    
@router.get("/upload_file")
async def upload_image(file: UploadFile):
    return {"filename" : file.filename}
