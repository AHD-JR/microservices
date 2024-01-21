from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.configs.db import client
from app.configs.cloudinary import configure_cloudinary
import os
from dotenv import load_dotenv
from app.api.category import router as category_router

load_dotenv()

app = FastAPI()

port = os.getenv('PORT')

origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

try:
    client.server_info()
    print("Connected to MongoDB 🚀")
except:
    print('Could not connect to MongoDB!')

try:
    configure_cloudinary()
    print("Cloudinary Configured 🚀")
except:
    print('Could not configure Cloudinary!')

@app.get('/')
async def root():
    return {"msg": f"Up and Runnning on port {port}..."}

app.include_router(category_router)