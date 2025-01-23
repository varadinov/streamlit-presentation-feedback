from pymongo import MongoClient
from config import config
from pymongo.server_api import ServerApi

mongo_client = MongoClient(config['MONGO_URI'], server_api=ServerApi('1'))