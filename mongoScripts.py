import pymongo
from pymongo import MongoClient
import datetime 

client = MongoClient("mongodb+srv://test-data-scraping:Parmar-123@data-scraping.pksegyo.mongodb.net/")

db = client.test            # test is our collection name
posts = db.test_collection   # here after . is the name of our database

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id = posts.insert_one(post).inserted_id
