# This was developed using iPython notebook, so the code should not necessarily be run straight through.

import pandas as pd
import json
from matplotlib.pyplot import cm
import matplotlib.colors as colors
import numpy as np

with open("coursetimes.json") as json_data:
    d = json.load(json_data)

data_dict = {}
departments = []
labels = []

for i in d:
    if i['Department'] not in data_dict:
        data_dict[i['Department']] = {}
    if i['Time'].split("-")[0].strip() not in labels:
        labels.append(i['Time'].split("-")[0].strip())

labels = sorted(labels)

# labels = ['8:00 a.m.', '8:30 a.m.', '8:40 a.m.', '8:45 a.m.', '9:00 a.m.', '9:30 a.m.', '10:00 a.m.', '10:30 a.m.', '11:00 a.m.', '11:20 a.m.', '11:30 a.m.', '12:00 p.m.', '12:30 p.m.', '1:00 p.m.', '1:15 p.m.', '1:30 p.m.', '2:00 p.m.', '2:15 p.m.', '2:30 p.m.', '3:00 p.m.', '3:30 p.m.', '4:00 p.m.', '4:15 p.m.', '4:30 p.m.', '5:00 p.m.', '5:30 p.m.', '6:00 p.m.', '6:30 p.m.', '7:00 p.m.', '7:15 p.m.']
print(labels)

real_times = ['8:00 a.m.', '8:30 a.m.', '8:40 a.m.', '8:45 a.m.', '9:00 a.m.', '9:30 a.m.', '10:00 a.m.', '10:30 a.m.', '11:00 a.m.', '11:20 a.m.', '11:30 a.m.', '12:00 p.m.', '12:30 p.m.', '1:00 p.m.', '1:15 p.m.', '1:30 p.m.', '2:00 p.m.', '2:15 p.m.', '2:30 p.m.', '3:00 p.m.', '3:30 p.m.', '4:00 p.m.', '4:15 p.m.', '4:30 p.m.', '5:00 p.m.', '5:30 p.m.', '6:00 p.m.', '6:30 p.m.', '7:00 p.m.', '7:15 p.m.']
stored_times = ['8:00 a.m.', '8:30 a.m.', '8:30 a.m.', '8:30 a.m.', '9:00 a.m.', '9:30 a.m.', '10:00 a.m.', '10:30 a.m.', '11:00 a.m.', '11:30 a.m.', '11:30 a.m.', '12:00 p.m.', '12:30 p.m.', '1:00 p.m.', '1:00 p.m.', '1:30 p.m.', '2:00 p.m.', '2:00 p.m.', '2:30 p.m.', '3:00 p.m.', '3:30 p.m.', '4:00 p.m.', '4:00 p.m.', '4:30 p.m.', '5:00 p.m.', '5:30 p.m.', '6:00 p.m.', '6:30 p.m.', '7:00 p.m.', '7:00 p.m.']
key_lookup = dict(zip(real_times, stored_times))

final_times = set(stored_times)
print(final_times)
print(stored_times)

for key in data_dict:
    for i in stored_times:
        data_dict[key][i] = 0
print(data_dict)

for i in d:
    dept = i["Department"]
    t = key_lookup[i['Time'].split("-")[0].strip()]
    data_dict[dept][t] += 1