from bs4 import BeautifulSoup
import requests
import json

url = 'http://www.gocrimson.com/landing/index'

roster_urls = []

result = requests.get(url)
page = result.content

soup = BeautifulSoup(page, "html.parser")

teams = soup.find("li", class_=lambda value: value and value.startswith("has-submenu"))
rosters = teams.find_all(attrs={"data-title": "Roster"})
for link in rosters:
    roster_urls.append('http://www.gocrimson.com' + link.get('href'))

counter = 0
biolist = [[] for i in range(len(roster_urls))]

for url in roster_urls:
    if counter == 23 or counter == 37:
        counter += 1
        continue
    else:
        result = requests.get(url)
        page = result.content

        key = url
        removals = ["http://www.gocrimson.com", "roster", "-include"]
        for removal in removals:
            key = key.replace(removal, '')

        key = key + "bios"

        soup = BeautifulSoup(page, "html.parser")
        if 'include' in url:
             parsed = soup.find("div", id='mainbody')
        else:
            parsed = soup.find("div", class_='roster')

        players = parsed.find_all(href=lambda value: value and value.startswith(key))

        for link in players:
            biolist[counter].append(link.get('href'))
        counter += 1

concentrations = {}
for x in range(0,40):
    print(x)
    for url in biolist[x]:
        url = 'http://www.gocrimson.com' + url

        result = requests.get(url)
        page = result.content

        soup = BeautifulSoup(page, "html.parser")
        interm = soup.find("td", string = "Major: ")
        if not interm:
            continue
        else:
            parsed = interm.find_next_sibling("td").get_text()
            if parsed not in concentrations:
                concentrations[parsed] = 1
            else:
                concentrations[parsed] += 1

with open('A_Concentrations.txt', 'w') as outfile:
    json.dump(concentrations, outfile)