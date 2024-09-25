import json
import requests
import sqlite3
import datetime
import matplotlib.pyplot as plt
import pandas as pd

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

count = 0
# loop through entire data set
for data in load_js:
    count = count + 1
    
    activityid = count
    lobbyistid = data.get("primarylobbyistid")
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

# commit to make sure all data is saved
conn.commit()
conn.close()

# create bar chart using loop
from collections import Counter

report_months = [entry.get('reportmonth') for entry in load_js]
month_counts = Counter(report_months)

months = list(month_counts.keys())
counts = list(month_counts.values())

plt.bar(months, counts, color='blue')

plt.title('Number of Lobbyists by Report Month')
plt.xlabel('Report Month')
plt.ylabel('Number of Lobbyists')

# create column chart using pivot table and Dataframe
df = pd.DataFrame(load_js)

pivot_table = df.pivot_table(index='reportmonth', aggfunc='size')

pivot_table.plot(kind='bar', color='blue')

plt.title('Number of Lobbyists by Report Month')
plt.xlabel('Report Month')
plt.ylabel('Number of Lobbyists')

plt.show()
