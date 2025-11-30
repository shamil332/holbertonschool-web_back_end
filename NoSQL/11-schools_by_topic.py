#!/usr/bin/env python3
""" a Python function that returns the list of school having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """Return a list of school documents"""
    if mongo_collection is None or not topic:
        return []
    return list(mongo_collection.find({"topics": topic}))
