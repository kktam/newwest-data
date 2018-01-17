import numpy as np
import pandas as pd
import json
import time

def parse_float(x):
    try:
        x = float(x)
    except Exception:
        x = 0
    return x
	
import datetime
def parse_full_date(row):
    date = datetime.datetime.strptime(row["date_of_stop"], "%Y-%m-%dT%H:%M:%S")
    time = row["time_of_stop"].split(":")
    date = date.replace(hour=int(time[0]), minute = int(time[1]), second = int(time[2]))
    return date	

fileUrl = 'SAFE_SCHOOL_ROUTES.json'

json_data=open(fileUrl).read()
data = json.loads(json_data)
data = pd.io.json.json_normalize(data)

routes = pd.DataFrame(data)
counts = routes["NAME"].value_counts()

# print (data)
print (counts)

import matplotlib.pyplot as plt

plt.xlabel('Name')
plt.ylabel('Count')
plt.hist(routes["NAME"], bins=10)
plt.show()
