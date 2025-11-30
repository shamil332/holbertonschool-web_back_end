#!/usr/bin/env python3
"""a Python function that inserts a new document in a collection based on kwargs"""
def insert_school(mongo_collection, **kwargs):
    if mongo_collection is None or not kwargs:
        return None
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
