import json
from typing import Dict
import requests

class RestIOClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            'cache-control': "no-cache",
            "x-apikey": api_key,
        }

    def create(self, data: Dict):
        response = requests.post(self.base_url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def read_all(self):
        response = requests.get(self.base_url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def read_by_id(self, record_id: str):
        url = f"{self.base_url}/{record_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def read_by_query(self, query):
        query_params = { 'q': json.dumps(query)}
        response = requests.get(self.base_url, headers=self.headers, params=query_params)
        response.raise_for_status()
        return response.json()
    
    def update(self, record_id: str, updated_data: Dict):
        url = f"{self.base_url}/{record_id}"
        response = requests.put(url, headers=self.headers, json=updated_data)
        response.raise_for_status()
        return response.json()

    def delete(self, record_id: str):
        url = f"{self.base_url}/{record_id}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return response.status_code