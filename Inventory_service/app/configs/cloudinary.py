from fastapi import UploadFile
import asyncio
import cloudinary
from cloudinary.uploader import upload
from cloudinary import api
import os
from dotenv import load_dotenv
from app.utils.response import response

load_dotenv()

name = os.environ.get('CLOUD_NAME')
key = os.environ.get('CLOUD_API_KEY')
secret = os.environ.get('CLOUD_API_SECRET')

def configure_cloudinary():      
    cloudinary.config( 
    cloud_name = name, 
    api_key = key, 
    api_secret = secret
    )


async def media_upload(photo: UploadFile, folder_name: str):
    try:
        res = await asyncio.to_thread(upload, photo.file, folder=folder_name)
        data = {
            "public_id": res['public_id'],
            "secure_url": res['secure_url']
        }
        
        return data
    except Exception as e:
        print(e)
        return response(status_code=400, message=str(e))
    

async def media_deletion(public_id: str):
    try:
        res = await asyncio.to_thread(api.delete_resources, [public_id])

        if res["deleted"][public_id] == "deleted":
            return response(status_code=200, message="Profile photo is removed!")

        return
    except Exception as e:
        return response(status_code=400, message=str(e))

