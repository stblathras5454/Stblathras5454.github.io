from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB without authentication"""

    def __init__(self):
        # Connect to MongoDB (no username/password required)
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['AAC']

    # CREATE
    def create(self, data):
        if data is not None:
            insert_result = self.database.animals.insert_one(data)  # data should be dictionary
            return insert_result.acknowledged
        else:
            raise Exception("No data to save, because data parameter is empty")

    # READ
    def read(self, query):
        if query is not None:
            return list(self.database.animals.find(query))
        else:
            return list(self.database.animals.find())

    # UPDATE
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            update_result = self.database.animals.update_many(query, {'$set': new_values})
            return update_result.modified_count
        else:
            raise Exception("Query or update data missing")

    # DELETE
    def delete(self, query):
        if query is not None:
            delete_result = self.database.animals.delete_many(query)
            return delete_result.deleted_count
        else:
            raise Exception("Nothing to delete, query is empty")
