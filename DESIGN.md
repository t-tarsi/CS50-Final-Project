For our data scraping algorithm, we used Beautiful Soup which is a Python library which allows us to get data from HTML files.
For conscrape.py, which allowed us to get the concentrations of each athlete, we first created a list to store URLs for each roster
page.

For the raw data tab, we executed the same procedure for both data sets. We first read in JSON data to python. Then we took the JSON data, looped through it and stored it as lists. Then we converted those lists into a Pandas dataframe, and outputted that data frame as an HTML table using pandas.to_html method. Then we took that table and placed it into our original html templates. This is why our raw data template is so large (it has every data point from the original JSON data). But it displays nicely, and we thought it was important to include because to our knowledge, this data has never been studied before.

For the data visualization, we primarily used Charts.js, a JavaScript library used for creating charts and other visualizations.
We modified Charts.js slightly: when a legend item was deselected, previously it would display as red. This was not visually appealing, so we changed it to display as grey when deselected.

The first two charts are donut charts displaying the proportion of athletes and non-athletes in certain concentrations. For the non-athlete data, we used Harvard Open Data Project's publicly available concentration data. For the athlete data, we used the data from our web scraper (see above). We used the "$.getJSON" function to grab our data in each instance. (We had set up routes to pass the necessary data for each chart. The routes are "/concentrations" for all students and "/AthleteConcentrations" for athletes)

The second display is a multi-line graph that shows the distribution of coursetimes for each Department. In order to display the data how we wanted, we needed to reformat it from its original form. This method can be seen in "scrapers/reformat_coursetimes.py".
To summarize, we looped through all of the course data, tracked each coursetime and department, reformatted the coursetimes to be in order, then looped through the data again and added 1 to our dictionary for each department's course at a given time. We ended with a python dictionary with keys being departments, each department had a list of coursetimes, and the number of coursetimes for that timeslot.

Then in JavaScript (in our "static/scripts.js" file), we took this data and used the keys (departments) as label items. For each department we used the keys (coursetimes) as the x-axis labels and the values (number of courses) as the y-axis values. We used a multi-line chart so that every department can be seen. The default, however, is that none are shown. Simply click on a department to see it's distribution of coursetimes.

For designing our about and team page, we used Bootstrap 4. We used this because we thought that Bootstrap's grid component would be
very useful and aesthetically pleasing our pages. The 12-column grid was helpful for both the bio page and the about page.
