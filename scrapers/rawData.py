# This file was necessary to take the raw JSON data, convert it to a pandas dataFrame, and output it as an html table.
# We then took that html table and put it into the data.html page to hold all of our raw data.

import pandas as pd
import json

# open concentration data
with open("data/A_Concentrations.json") as json_data:
        f = json.load(json_data)
with open("data/StudentConcentrations.json") as json_data:
        j = json.load(json_data)

# Store the data as lists, taken from the dict from the JSON data
Concentration = list(f.keys())
AthleteConcentrators = list(f.values())
TotalConcentrators = list(j.values())

# Store as a dataframe
raw_data = pd.DataFrame({
        "Concentration": Concentration,
        "Total Concentrators": TotalConcentrators,
        "Athlete Concentrators": AthleteConcentrators
})

# Convert this dataframe into an html table, outputted as the file "rawConcentrationData.html". We then took this table and pasted it into "data.html"
# Moved into the data folder
raw_data.to_html("rawConcentrationData.html")

# open up the coursetime JSON data
with open("data/new_coursetimes.json") as json_data:
     f = json.load(json_data)

# Initialize necessary lists
depts = []
numCourses = []
times= []

# Loop through each key in the JSON data
for key in f:
    # Save the times in a list
    times_temp = list(f[key].keys())
    # save the number of courses for each timeslot into a list
    numCourses_temp = list(f[key].values())

    # Ensure the correct number of department iterations. It must match the number of instances of the timeslots and the numCourses array, because of the nature of Pandas dataframes
    for i in range(len(times_temp)):
        depts.append(key)
    # Add each number of courses count into a list
    for i in numCourses_temp:
        numCourses.append(i)
    # Add each coursetime into a list for each department
    for i in times_temp:
        times.append(i)

# Save this data as a pandas dataframe
raw_data = pd.DataFrame({
    "Department": depts,
    "Times": times,
    "Number of Courses": numCourses
})

# Export the data as an HTML table the the file named below. Pasted into "data.html" and then moved to the data folder
raw_data.to_html("rawCourseData.html")