from bs4 import BeautifulSoup
import requests
import json

departments = []
courses = []
times = []

# Loop through each page range on course catalog
for start in range(0, 1400, 100):
    page_url = "https://courses.harvard.edu/search?fq_credit_level=credit_level%3A%22Undergraduate%22&fq_school_nm=school_nm%3A%22Faculty%20of%20Arts%20and%20Sciences%22&fq_term_desc=term_desc%3A%22Fall%202016-2017%22&q=&sort=course_title%20asc&start={}&rows=100".format(start)

    result = requests.get(page_url)
    page = result.content

    # Parse html using Beautiful Soup 4
    soup = BeautifulSoup(page, "html.parser")

    # Get course name and time
    courses_html = soup.find_all(id="srl_title")
    times_html = soup.find_all(class_="time")

    # Set trackers for courses that don't have times
    marker = 0
    timeless_courses = []

    # Parse courses and times into an array
    for time in times_html:
        time = time.string

        # Check to see if course has a time
        if time[0].isalpha() == False:
            times.append(time)
            marker += 1

        elif ";" in time:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            for x in range(0,5):
                time = time.replace(days[x], '')
            times.append(time)
            marker += 1

        else:
            timeless_courses.append(marker)
            marker += 1

    marker = 0

    for course in courses_html:
        if marker not in timeless_courses:
            course = course.string

            # Split scraped course name into course title and department
            department,course = course.split("-", 1)
            department = department.rsplit()[0]

            courses.append(course)
            departments.append(department)
            marker += 1

        else:
            marker += 1
lst = []

# Add dicts to list
for x in range(0,1096):
    data = {}
    data.update({'Name': courses[x], 'Department': departments[x], 'Time': times[x]})
    lst.append(data)

# Convert to json and save to text file
with open('data.txt', 'w') as outfile:
    json.dump(lst, outfile)