import os
from dotenv import load_dotenv
load_dotenv()

config = {
    "MONGO_URI": os.environ['MONGO_URI'],
    "MONGO_DB": 'feedbackdb',
    "OAUTH2_CLIENT_ID": os.environ['OAUTH2_CLIENT_ID'],
    "OAUTH2_CLIENT_SECRET": os.environ['OAUTH2_CLIENT_SECRET'],
    "OAUTH2_REDIRECT_URI": os.environ['OAUTH2_REDIRECT_URI'],
}
