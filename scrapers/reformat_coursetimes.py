# This was developed using iPython notebook, so the code should not necessarily be run straight through.

import pandas as pd
import json
from matplotlib.pyplot import cm
import matplotlib.colors as colors
import numpy as np

# Open coursetimes data as a JSON file
with open("coursetimes.json") as json_data:
    d = json.load(json_data)

# Establish necessary variables. data_dict is the final form that will be outputted
data_dict = {}
departments = []
labels = []

# Loop through all of the course data
for i in d:

    # Add each unique department as a key in our data_dict, each with a Dict of it's own
    if i['Department'] not in data_dict:
        data_dict[i['Department']] = {}

    # Add each course time into our labels array. This will be useful later.
    if i['Time'].split("-")[0].strip() not in labels:
        labels.append(i['Time'].split("-")[0].strip())

# This sorts the labels, but they are still not in order by time. So we printed the labels and manually rearranged them. Recall, this was an ipython notebook so that was very easy.
labels = sorted(labels)

# labels = ['8:00 a.m.', '8:30 a.m.', '8:40 a.m.', '8:45 a.m.', '9:00 a.m.', '9:30 a.m.', '10:00 a.m.', '10:30 a.m.', '11:00 a.m.', '11:20 a.m.', '11:30 a.m.', '12:00 p.m.', '12:30 p.m.', '1:00 p.m.', '1:15 p.m.', '1:30 p.m.', '2:00 p.m.', '2:15 p.m.', '2:30 p.m.', '3:00 p.m.', '3:30 p.m.', '4:00 p.m.', '4:15 p.m.', '4:30 p.m.', '5:00 p.m.', '5:30 p.m.', '6:00 p.m.', '6:30 p.m.', '7:00 p.m.', '7:15 p.m.']
print(labels)

# Consolidate the coursetimes into 30 minute intervals, utilizing a dictionary. As were looping through the data, this will be used to determine with key each coursetime will be associated with. Crucial for the coursetimes that are not at 30 min intervals (i.e. 8:40, 9:15)
real_times = ['8:00 a.m.', '8:30 a.m.', '8:40 a.m.', '8:45 a.m.', '9:00 a.m.', '9:30 a.m.', '10:00 a.m.', '10:30 a.m.', '11:00 a.m.', '11:20 a.m.', '11:30 a.m.', '12:00 p.m.', '12:30 p.m.', '1:00 p.m.', '1:15 p.m.', '1:30 p.m.', '2:00 p.m.', '2:15 p.m.', '2:30 p.m.', '3:00 p.m.', '3:30 p.m.', '4:00 p.m.', '4:15 p.m.', '4:30 p.m.', '5:00 p.m.', '5:30 p.m.', '6:00 p.m.', '6:30 p.m.', '7:00 p.m.', '7:15 p.m.']
stored_times = ['8:00 a.m.', '8:30 a.m.', '8:30 a.m.', '8:30 a.m.', '9:00 a.m.', '9:30 a.m.', '10:00 a.m.', '10:30 a.m.', '11:00 a.m.', '11:30 a.m.', '11:30 a.m.', '12:00 p.m.', '12:30 p.m.', '1:00 p.m.', '1:00 p.m.', '1:30 p.m.', '2:00 p.m.', '2:00 p.m.', '2:30 p.m.', '3:00 p.m.', '3:30 p.m.', '4:00 p.m.', '4:00 p.m.', '4:30 p.m.', '5:00 p.m.', '5:30 p.m.', '6:00 p.m.', '6:30 p.m.', '7:00 p.m.', '7:00 p.m.']
key_lookup = dict(zip(real_times, stored_times))

# final_times = set(stored_times)
# print(final_times)
# print(stored_times)

# Loop through each Key (department) in the data_dict. Add a set of new keys (the coursetimes) to each department, and initialize the value of each to 0. This will be used to track how many courses there are for each timeslot for each Department.
for key in data_dict:
    for i in stored_times:
        data_dict[key][i] = 0
# print(data_dict)

# Now loop through the original data
for i in d:

    # establish a department variable. This value is the department for the current course.
    dept = i["Department"]

    # establish a t (timeslot) variable, using the dict from before. This value is the coursetime for the current course
    t = key_lookup[i['Time'].split("-")[0].strip()]

    # Now that we know the department and timeslot for the current course, add 1 to the counter for this Department-Course combo in our data_dict
    data_dict[dept][t] += 1

    # This data dict was outputted, saved, and uploaded to the data folder as new_coursetimes