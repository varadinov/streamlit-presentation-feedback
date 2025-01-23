
from utils.feedback_service import FeedBackService
from config import config
from db import mongo_client

feedback_service = FeedBackService(mongo_client, config['MONGO_DB'])