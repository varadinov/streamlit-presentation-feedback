from config import config
from utils.restio_client import RestIOClient

restio_client = RestIOClient(config['RESTIO_URL'], config['RESTIO_KEY'])