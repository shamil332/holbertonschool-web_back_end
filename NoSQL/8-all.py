#!/usr/bin/python3
# a Python function that lists all documents in a collection
def list_all(mongo_collection):
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
