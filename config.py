import os
from dotenv import load_dotenv
load_dotenv()

config = {
    "RESTIO_URL": "https://streamlit-a9b5.restdb.io/rest/feedback", 
    "RESTIO_KEY": os.environ['RESTIO_KEY'],
    "OAUTH2_CLIENT_ID": os.environ['OAUTH2_CLIENT_ID'],
    "OAUTH2_CLIENT_SECRET": os.environ['OAUTH2_CLIENT_SECRET'],
    "OAUTH2_REDIRECT_URI": os.environ['OAUTH2_REDIRECT_URI'],
}
