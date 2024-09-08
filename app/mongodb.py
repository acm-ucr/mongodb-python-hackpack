'''MongoDB File'''
import os.path
import os
from dotenv import load_dotenv
from pymongo import MongoClient


class MongoDB:
    '''MongoDB Class'''

    def __init__(self):
        self.collection = None
        self._connect_db()

    def _connect_db(self):
        '''Private method to connect to the MongoDB database.'''
        load_dotenv()
        uri = os.getenv("MONGODB_URI")
        client = MongoClient(uri)
        db = client["users"]
        self.collection = db["accounts"]

    def create_document(self, data):
        '''Inserts a document into the collection.'''
        if self.collection is None:
            print("Error: Database not connected.")
            return
        result = self.collection.insert_one(data)
        print(f"Inserted document ID: {result.inserted_id}")

    def read_documents(self, query=None):
        '''Reads documents from the collection based on the given query.'''
        query = query or {}
        results = self.collection.find(query)
        for doc in results:
            print(doc)

    def update_document(self, query, update):
        '''Updates a document in the collection based on the given query.'''
        result = self.collection.update_one(query, {"$set": update})
        if result.matched_count:
            print("User account updated successfully.")
        else:
            print("No user account found with the given query.")

    def update_many_documents(self, query, update):
        '''Updates a document in the collection based on the given query.'''
        result = self.collection.update_many(query, {"$set": update})
        if result.matched_count:
            print("User accounts updated successfully.")
        else:
            print("No users found with the given query.")

    def delete_document(self, query):
        '''Deletes a document from the collection based on the given query.'''
        result = self.collection.delete_one(query)
        if result.deleted_count:
            print("User account deleted successfully.")
        else:
            print("No user account found with the given query.")

    def delete_many_documents(self, query):
        '''Deletes a document from the collection based on the given query.'''
        result = self.collection.delete_many(query)
        if result.deleted_count:
            print(f"{result.deleted_count} accounts deleted successfully.")
        else:
            print("No users found with the given query.")
