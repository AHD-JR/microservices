from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get('MONGODB_URL')
DB_URL = "mongodb+srv://ahmadmauwal20:GQU4bEeWwyG2q3pN@cluster0.qlgnm4c.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(DB_URL)
db = client['inventory_service']

product_collection = db['products']
category_collection = db['category']
order_collection = db['order']
