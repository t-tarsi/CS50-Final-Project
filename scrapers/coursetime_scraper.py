from bs4 import BeautifulSoup
import requests

page_url = "https://courses.harvard.edu/search?fq_coordinated_semester_yr=coordinated_semester_yr%3A%22Sep+to+Dec+2016+%28Fall+Term%29%22&fq_school_nm=school_nm%3A%22Faculty+of+Arts+and+Sciences%22&q=&sort=course_title+asc&start=0&submit=Search"

# Get page html
result = requests.get(page_url)
page = result.content

# Parse html using Beautiful Soup 4
soup = BeautifulSoup(page, "html.parser")

# Get course html
courses_html = soup.find_all(id="srl_title")

# Parse courses into an array
courses = []
for course in courses_html:
    courses.append(course.string)