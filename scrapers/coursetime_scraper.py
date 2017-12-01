from bs4 import BeautifulSoup
import requests

courses = []
# Loop through each page range
for start in range(0, 1400, 100):
    page_url = "https://courses.harvard.edu/search?fq_credit_level=credit_level%3A%22Undergraduate%22&fq_school_nm=school_nm%3A%22Faculty%20of%20Arts%20and%20Sciences%22&fq_term_desc=term_desc%3A%22Fall%202016-2017%22&q=&sort=course_title%20asc&start={}&rows=100".format(start)

    result = requests.get(page_url)
    page = result.content

    # Parse html using Beautiful Soup 4
    soup = BeautifulSoup(page, "html.parser")

    # Get course html
    courses_html = soup.find_all(id="srl_title")

    # Parse courses into an array
    for course in courses_html:
        courses.append(course.string)

