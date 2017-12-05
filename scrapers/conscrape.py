from bs4 import BeautifulSoup
import requests
import json

# Index page on website that data will be scraped from
url = 'http://www.gocrimson.com/landing/index'

# Create list to store urls to each roster page
roster_urls = []

# Open up page and make soup
result = requests.get(url)
page = result.content
soup = BeautifulSoup(page, "html.parser")

# Scrape links to each roster for each team
teams = soup.find("li", class_=lambda value: value and value.startswith("has-submenu"))
rosters = teams.find_all(attrs={"data-title": "Roster"})
for link in rosters:
    roster_urls.append('http://www.gocrimson.com' + link.get('href'))

# Set list of lists for storing each athlete page in each team roster
# Create counter to count out duplicate rosters of "co-ed" teams (i.e. track, skiing)
counter = 0
biolist = [[] for i in range(len(roster_urls))]

# Iterate through rosters pages and scrape urls for each athletes page
for url in roster_urls:

    # Skip duplicate rosters
    if counter == 23 or counter == 37:
        counter += 1
        continue
    else:
        result = requests.get(url)
        page = result.content

        # Format urls for rosters from scraped roster routes
        key = url
        removals = ["http://www.gocrimson.com", "roster", "-include"]
        for removal in removals:
            key = key.replace(removal, '')

        key = key + "bios"

        # Make soup and scrape for athlete bio links
        soup = BeautifulSoup(page, "html.parser")
        if 'include' in url:
             parsed = soup.find("div", id='mainbody')
        else:
            parsed = soup.find("div", class_='roster')

        players = parsed.find_all(href=lambda value: value and value.startswith(key))

        # Add scraped athlete bio urls to list of lists
        for link in players:
            biolist[counter].append(link.get('href'))
        counter += 1

# Make dict to store number of concentrators in each concentration
concentrations = {}

# Iterate through each roster list in list of lists
for x in range(0,40):

    # Progress check to see how far through the scraping script is
    print(x)

    # Iterate through each scraped athlete route in roster
    for url in biolist[x]:

        # Format scraped athlete bio routes
        url = 'http://www.gocrimson.com' + url

        # Make soup for scraping concentrations
        result = requests.get(url)
        page = result.content

        # Scrape concentrations
        soup = BeautifulSoup(page, "html.parser")
        interm = soup.find("td", string = "Major: ")

        # Skip if athlete does not have concentration
        if not interm:
            continue

        # Add concentration to dict if it does not exist, else increase count
        else:
            parsed = interm.find_next_sibling("td").get_text()
            if parsed not in concentrations:
                concentrations[parsed] = 1
            else:
                concentrations[parsed] += 1

# Convert dict to JSON and save to outfile
with open('A_Concentrations.json', 'w') as outfile:
    json.dump(concentrations, outfile)