#!/usr/bin/env python
# coding: utf-8

# In[115]:


# Thi Phan

import json
import requests
import sqlite3
import datetime


# In[116]:


# connect to the output database
conn = sqlite3.connect('spring.sqlite')
# forces database to return strings for text attributes
conn.text_factory = str
# get the cursor for the connection
cur = conn.cursor()
# drop the tables
cur.executescript('''DROP TABLE IF EXISTS Lobbyist''')
# read data from file created
file = open("data.txt", "r")
read_js = file.read()
load_js = json.loads(read_js)

# create the tables 
cur.executescript('''CREATE TABLE IF NOT EXISTS Lobbyist (
    activityid INTEGER PRIMARY KEY,
    primarylobbyistid TEXT, 
    lobbyistlastname TEXT, 
    lobbyistaddress1 TEXT, 
    lobbyistcity TEXT, 
    lobbyiststate TEXT, 
    incomeamount REAL, 
    fiscalyear INTEGER, 
    dateincomereceived TEXT)''')

print("\nFirst Lobbyist List")
print(load_js[0])


# In[117]:


count = 0
# loop through entire data set
for data in load_js:
    count = count + 1
    
    activityid = count
    lobbyistid   = data.get("primarylobbyistid")
    name    = data.get("lobbyistlastname")
    address = data.get("lobbyistaddress1")
    city    = data.get("lobbyistcity")
    state   = data.get("lobbyiststate")
    income  = data.get("incomeamount", None)
    year    = data.get("fiscalyear", None)
    date    = data.get("dateincomereceived", None)
    
    cur.execute('''INSERT INTO Lobbyist(activityid, primarylobbyistid, lobbyistlastname, lobbyistaddress1, lobbyistcity, lobbyiststate, incomeamount, fiscalyear, dateincomereceived)
    VALUES (?,?,?,?,?,?,?,?,?)''',
                (activityid, lobbyistid, name, address, city, state, income, year, date))
    
    if count%100==0:
        print("\nThere has been", count, "number of readings")
        conn.commit()
   


# In[118]:


# commit to make sure all data is saved
conn.commit()
conn.close()

