# This file was necessary to take the raw JSON data, convert it to a pandas dataFrame, and output it as an html table.
# We then took that html table and put it into the data.html page to hold all of our raw data.

import pandas as pd
import json

with open("scrapers/A_Concentrations.json") as json_data:
        f = json.load(json_data)
with open("data/StudentConcentrations.json") as json_data:
        j = json.load(json_data)
Concentration = list(f.keys())
AthleteConcentrators = list(f.values())
TotalConcentrators = list(j.values())

raw_data = pd.DataFrame({
        "Concentration": Concentration,
        "Total Concentrators": TotalConcentrators,
        "Athlete Concentrators": AthleteConcentrators
})
raw_data.to_html("data.html")

with open("data/new_coursetimes.json") as json_data:
     f = json.load(json_data)
depts = []
numCourses = []
times= []
for key in f:
    times_temp = list(f[key].keys())
    numCourses_temp = list(f[key].values())
    for i in range(23):
        depts.append(key)
    for i in numCourses_temp:
        numCourses.append(i)
    for i in times_temp:
        times.append(i)
raw_data = pd.DataFrame({
    "Department": depts,
    "Times": times,
    "Number of Courses": numCourses
})
raw_data.to_html("rawdata.html")