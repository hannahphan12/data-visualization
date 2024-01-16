pip install pymongo

import pymongo

from pymongo import MongoClient

mongoClient = MongoClient("mongodb+srv://<username>:m001-mongodb-basics@sandbox.1l0o4r2.mongodb.net/?retryWrites=true&w=majority")

import json

import urllib.request, urllib.parse, urllib.error

import requests

import time

url = "https://data.colorado.gov/resource/gxnn-wthy.json"
paramD = dict()
paramD["id'"] = 7
paramD["$order"] = "timestamps DESC"
paramD["$limit"] = 5000

# create a database to hold JSON data
db = mongoClient["50"]

# create a collection to hold downloaded JSON readings
collection = db["assignment"]

# open the URL using the request library
document = requests.get(url,paramD)

# extract the entire data from JSON file
data = json.loads(document.content)
my_data = data

# add parameters
lobbyist = [{"primarylobbyistid": 20155006971}, {"primarylobbyistid": 19907000285}, {"primarylobbyistid": 20125002519}, {"primarylobbyistid": 20045003574}, {"primarylobbyistid": 20175002823}, {"primarylobbyistid": 20065004397}, {"primarylobbyistid": 19897000025}]

# get the number of readings in the JSON array downloaded
num_readings = len(data)
offset = 0

for i in [20155006971, 19907000285, 20125002519, 20045003574, 20175002823, 20065004397, 19897000025]:
    paramD["id"] = i
    params = urllib.parse.urlencode(paramD)
    if document.content != 200:
        data = json.loads(document.content)
        text = "{}"
    js = json.loads(text)
    offset = offset + len(js)
print("documents added to assignment collection")        
