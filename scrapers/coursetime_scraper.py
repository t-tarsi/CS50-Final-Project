from bs4 import BeautifulSoup
import requests
import json

departments = []
courses = []
times = []

# Make lists for later use in saving scraped data
departments = []
courses = []
times = []

# Loop through each page range on course catalog
for start in range(0, 1400, 100):
    page_url = "https://courses.harvard.edu/search?fq_coordinated_semester_yr=coordinated_semester_yr%3A%22Jan+to+May+2018+%28Spring+Term%29%22&fq_school_nm=school_nm%3A%22Faculty+of+Arts+and+Sciences%22&fq_credit_level=credit_level%3A%22Undergraduate%22&q=&sort=course_title%20asc&start={}&rows=100".format(start)

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

    # Parse times into an array
    for time in times_html:
        time = time.string

        # Check to see if course has a time
        if time[0].isalpha() == False:
            times.append(time)
            marker += 1

        # Check to see if course has multiple meeting times
        elif ";" in time:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            for x in range(0,5):
                time = time.replace(days[x], '')
            times.append(time)
            marker += 1

        # Get course time if previous two conditions are not met
        else:
            timeless_courses.append(marker)
            marker += 1

    marker = 0

    # Parse courses into an array
    for course in courses_html:
        if marker not in timeless_courses:
            course = course.string

            # Split scraped course name into course title and department
            if '-' in course:
                department,course = course.split("-", 1)
                department = department.rsplit()[0]

            courses.append(course)
            departments.append(department)
            marker += 1

        else:
            marker += 1
lst = []

# Add data from arrays to dictionary
for x in range(0,1074):
    data = {}
    data.update({'Name': courses[x], 'Department': departments[x], 'Time': times[x]})
    lst.append(data)

# Turn dict to JSON and save
with open('Spring2018.json', 'w') as outfile:
    json.dump(lst, outfile)