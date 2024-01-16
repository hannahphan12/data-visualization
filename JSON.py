#!/usr/bin/env python
# coding: utf-8

# In[19]:


pip install pymongo


# In[18]:


import pymongo


# In[14]:


from pymongo import MongoClient


# In[15]:


mongoClient = MongoClient("mongodb+srv://<username>:m001-mongodb-basics@sandbox.1l0o4r2.mongodb.net/?retryWrites=true&w=majority")


# In[23]:


import json


# In[33]:


import urllib.request, urllib.parse, urllib.error
import requests


# In[25]:


import time


# In[26]:


url = "https://data.colorado.gov/resource/gxnn-wthy.json"
paramD = dict()
paramD["id'"] = 7
paramD["$order"] = "timestamps DESC"
paramD["$limit"] = 5000


# In[27]:


# create a database to hold JSON data
db = mongoClient["50"]


# In[29]:


# create a collection to hold downloaded JSON readings
collection = db["assignment"]


# In[79]:


# open the URL using the request library
document = requests.get(url,paramD)


# In[49]:


# extract the entire data from JSON file
data = json.loads(document.content)
my_data = data


# In[115]:


# add parameters
lobbyist = [{"primarylobbyistid": 20155006971}, {"primarylobbyistid": 19907000285}, {"primarylobbyistid": 20125002519}, {"primarylobbyistid": 20045003574}, {"primarylobbyistid": 20175002823}, {"primarylobbyistid": 20065004397}, {"primarylobbyistid": 19897000025}]


# In[111]:


# get the number of readings in the JSON array downloaded
num_readings = len(data)
offset = 0


# In[116]:


for i in [20155006971, 19907000285, 20125002519, 20045003574, 20175002823, 20065004397, 19897000025]:
    paramD["id"] = i
    params = urllib.parse.urlencode(paramD)
    if document.content != 200:
        data = json.loads(document.content)
        text = "{}"
    js = json.loads(text)
    offset = offset + len(js)
print("documents added to assignment collection")        


# In[ ]:


# Thi Phan

