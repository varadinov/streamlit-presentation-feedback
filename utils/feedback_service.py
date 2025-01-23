from typing import Dict, Any
from pymongo.mongo_client import MongoClient

from bson.objectid import ObjectId

    
class FeedBackService:
    def __init__(self, mongo_client: MongoClient, database: str):
        self.client = mongo_client
        self.db = self.client[database]
        self.collection = self.db['feedbacks']

    def create(self, data: Dict[str, Any]):
        return self.collection.insert_one(data)

    def read(self, filter_criteria: Dict = None):
        documents = self.collection.find(filter_criteria)
        for doc in documents:
            yield doc

    def update(self, object_id: str, update_data: Dict) -> int:
        filter_criteria = {"_id": ObjectId(object_id)}
        result = self.collection.update_one(filter_criteria, {"$set": update_data})
        return result.modified_count 

    def delete(self, filter_criteria: Dict) -> int:
        result = self.collection.delete_many(filter_criteria)
        return result.deleted_count 