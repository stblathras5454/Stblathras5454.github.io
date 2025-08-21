from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB without authentication.
    
    [ENHANCEMENT] Refactored for improved input validation, error handling, and design clarity.
    """

    def __init__(self, host='localhost', port=27017, db_name='AAC'):
        """Initialize connection to MongoDB."""
        try:
            self.client = MongoClient(f'mongodb://{host}:{port}/', serverSelectionTimeoutMS=5000)
            self.client.server_info()  # [ENHANCEMENT] Triggers exception if server is unreachable
            self.database = self.client[db_name]
        except errors.ServerSelectionTimeoutError as err:
            raise ConnectionError(f"Could not connect to MongoDB: {err}")

    # CREATE
    def create(self, data):
        """Insert a new document into the animals collection."""
        if isinstance(data, dict) and data:
            try:
                result = self.database.animals.insert_one(data)
                return result.acknowledged
            except Exception as e:
                raise RuntimeError(f"Error inserting data: {e}")
        else:
            raise ValueError("Invalid input: data must be a non-empty dictionary.")  # [ENHANCEMENT]

    # READ
    def read(self, query=None, projection=None):
        """Query the animals collection with optional field projection."""
        try:
            if query and not isinstance(query, dict):
                raise ValueError("Query must be a dictionary.")  # [ENHANCEMENT]
            if projection and not isinstance(projection, dict):
                raise ValueError("Projection must be a dictionary.")
            return list(self.database.animals.find(query or {}, projection))  # [ENHANCEMENT]
        except Exception as e:
            raise RuntimeError(f"Error reading data: {e}")

    # UPDATE
    def update(self, query, new_values):
        """Update matching documents with new values."""
        if not isinstance(query, dict) or not isinstance(new_values, dict):
            raise ValueError("Both query and new_values must be dictionaries.")  # [ENHANCEMENT]
        if not query or not new_values:
            raise ValueError("Query and update values must not be empty.")  # [ENHANCEMENT]

        try:
            result = self.database.animals.update_many(query, {'$set': new_values})
            return result.modified_count
        except Exception as e:
            raise RuntimeError(f"Error updating data: {e}")

    # DELETE
    def delete(self, query):
        """Delete documents matching the query."""
        if not isinstance(query, dict) or not query:
            raise ValueError("Query must be a non-empty dictionary.")  # [ENHANCEMENT]
        try:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        except Exception as e:
            raise RuntimeError(f"Error deleting data: {e}")
