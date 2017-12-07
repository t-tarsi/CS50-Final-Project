DESIGN:

This file details our implementation and design for our entire project, including our web scrapers, our python data manipulation,
our JavaScript functionality, visualization, and libraries.

For our data scraping scripts, we used Beautiful Soup 4 which is a Python library used to parse HTML files and scrape data
from them. We wound up implementing two separate scraping scripts, the first being for every course name, department and
time on the course catalog site; this was the easier of the two to implement because there was only a single page which had
all of the data we were looking for. The only exceptions to this were that we had to change the url after scraping every 100
classes because the page had a cap of displaying only 500 results at a time (this was easy to change in the url though) and
then I manually went in and entered different urls for different semesters (i.e. Spring 2017, Fall 2016, etc.) (we wound up
scraping all of the course information from Fall 2016 through Spring 2018 and the files are in the data.html template and data
folder, but we only used the course data from Fall 2016 and Spring 2017 to ensure more robust final visualizations). We also had to
implement lines of code which would take into account classes that had multiple meeting times as well as classes that didn't
have times listed (to skip these). Overall, our data output was a JSON file which listed every class name, times meeting and
the department it was in.

The second data scraping script was a bit trickier. This data came from the Harvard Athletics website, but every
concentration is listed individually on the athlete bio pages. These bio pages in turn were only accessible from the team roster
pages, both the bios and rosters having fairly unique urls. So, we wrote a three tiered scraping script. This first scraped
the routes for each roster from the Harvard Athletics home page and saved them to a list. We then formatted each route in the
list and concatanated each to the common url for roster pages and put them into the second tier of the script which went through
each roster page and scraped the routes for each individual athlete on each team, saving them into a list of lists. Finally,
each of these routes was concatanated with the common link for each bio url and iterated through to scrape for concentrations.
Each concentration was then added to a dict, or that dict value added to if already in existence. This dict was then converted
into a json (after manual alterations for misspellings and adding concentrations which were listed differently but the same) to
be used in our visualizations. The scraping script took into account teams whose roster pages were "coed" or had both men
and women listed on the men and women roster links (our script skipped the duplicates), as well as athletes who did not have
concentrations (undeclared sophomores, freshmen).

For the raw data tab, we executed the same procedure for both data sets. We first read in JSON data to python. Then we took
the JSON data, looped through it and stored it as lists. Then we converted those lists into a Pandas dataframe, and
outputted that data frame as an HTML table using the pandas.to_html method. Then we took that table and placed it into our
original html template (data.html). This is why our raw data template is so large (it has every data point from the original JSON data).
But it displays nicely, and we thought it was important to include because to our knowledge, this data has never been
studied before.

For the data visualization, we primarily used Charts.js, a JavaScript library used for creating charts and other visualizations.
We modified Charts.js slightly: when a legend item was deselected, previously it would display as red. This was not visually
appealing, so we changed it to display as grey when deselected.

The first two charts are donut charts displaying the proportion of athletes and non-athletes in certain concentrations.
For the non-athlete data, we used Harvard Open Data Project's publicly available concentration data. For the athlete data, we
used the data from our web scraper (see above). We used the "$.getJSON" function to grab our data in each instance. (We had
set up routes to pass the necessary data for each chart. The routes are "/concentrations" for all students and
"/AthleteConcentrations" for athletes). For the athlete concentration data, we manually reformatted it to match the format of the HODP data.
So, we made sure every concentration had a key, whether or not that concentration had a non-zero value.
In order to make sure that each concentration was represented by the same color in both charts, we needed to declare a colors array
in scripts.js. The colors are for each concentration are then randomized and saved to this array. In turn, this array is used
for the color option of both donut charts, ensuring that the colors match.

The second display is a multi-line graph that shows the distribution of coursetimes for each Department. In order to display
the data how we wanted, we needed to reformat it from its original form. This method can be seen in
"scrapers/reformat_coursetimes.py" (this was originally implemented as an iPython notebook). To summarize, we looped through all of the course data, tracked each coursetime and
department, reformatted the coursetimes to be in order, then looped through the data again and incremented our counter by 1 to our dictionary
for each department's course at a given time. We ended with a python dictionary with keys being departments, each department
had a list of coursetimes, and the number of coursetimes for that timeslot.

Then in JavaScript (in our "static/scripts.js" file), we took this data and used the keys (departments) as label items. For
each department we used the keys (coursetimes) as the x-axis labels and the values (number of courses) as the y-axis values.
We used a multi-line chart so that every department can be seen. The default, however, is that none are shown. Simply click
on a department to see it's distribution of coursetimes.

We also borrowed a randomized color function from StackOverflow. Here is the link: https://stackoverflow.com/questions/45771849/chartjs-random-colors-for-each-part-of-pie-chart-with-data-dynamically-from-data

For designing our about and team page, we used Bootstrap 4. We used this because we thought that Bootstrap's grid component
would be very useful and aesthetically pleasing our pages. The 12-column grid was helpful for both the bio page and the about
page.
