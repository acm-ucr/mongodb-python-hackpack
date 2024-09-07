'''Main File'''
from app.mongodb import MongoDBHandler


def main():
    '''Main Function'''
    db_handler = MongoDBHandler()

    db_handler.create_document({"name": "Alice", "email": "alice21@gmail.com"})

    print("\nDocuments in collection:")
    db_handler.read_documents()

    db_handler.update_document({"name": "Alice"},
                               {"email": "alice12@gmail.com"})

    print("\nDocuments after update:")
    db_handler.read_documents()

    db_handler.delete_document({"name": "Alice"})

    print("\nDocuments after deletion:")
    db_handler.read_documents()
