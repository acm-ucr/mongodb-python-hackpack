'''Main File'''
from app.mongodb import MongoDB


def main():
    '''Main Function'''
    db_handler = MongoDB()

    db_handler.create_document({
        "name": "Alice",
        "email": "alice21@gmail.com",
        "status": "inactive"
    })
    db_handler.create_document({
        "name": "Alex",
        "email": "alex123@gmail.com",
        "status": "inactive"
    })
    db_handler.create_document({
        "name": "Bryan",
        "email": "byran90@gmail.com",
        "status": "inactive"
    })
    db_handler.create_document({
        "name": "Beckie",
        "email": "beckie231@gmail.com",
        "status": "inactive"
    })

    print("\nDocuments in collection:")
    db_handler.read_documents()

    db_handler.update_document({"name": "Alice"},
                               {"email": "alice12@gmail.com"})
    print("\nDocuments after updating one document:")
    db_handler.read_documents()

    print("\nDocuments after updating many documents:")
    db_handler.update_many_documents({"name": {
        "$regex": "^A"
    }}, {"status": "active"})
    db_handler.read_documents()

    db_handler.delete_document({"name": "Alice"})
    print("\nDocuments after deletion:")
    db_handler.read_documents()

    db_handler.delete_many_documents({"status": "active"})
    print("\nDocuments after deleting many documents:")
    db_handler.read_documents()
