from pymongo import MongoClient

def create_collection():
    client = MongoClient('localhost', 27017)
    db = client['example_db']
    collection = db['users']
    return collection

if __name__ == "__main__":
    collection = create_collection()

