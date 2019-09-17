# cs50 final project
CS50 Final Project for Tyler Tarsi, Aaron Kruk, and LJ Barlow.

For our project, we sought out data on the underrepresentation of student-athletes (vs. non-athletes) in certain concentrations.
To do this we looked a coursetimes for every course in the Harvard Registrar. We believe that coursetimes may have an influence on students concentration selection, as most athletes are busy during the 3pm-6pm timeslot.
Then, we created a framework for analyzing this data through visualization. In order to view our site, please run Flask using the standard Flask setup.

Our About page on our website gives more insight on our project. It describes what we are trying to answer: the question of whether or not
student athletes concentrate more heavily in certain concentrations, and if so, is it because of time constraints on courses. It also describes
how we formulated the website and how we are giving the framework needed for one to answer the question.

Our Team page gives an introduction to each of our team members and has a bio about for of us. It has pictures of each of
us and a link to our respective pages on GoCrimson.

Our Raw Data page has our data in 2 HTML tables. We used a JSON file and transferred it to a pandas dateframe. Then, in python,
we converted the dataframe to an HTML table, and copy and pasted the table into our HTML template. We thought it was important to include this data, because (to our knowledge) it has never been studied before. (besides the Harvard Open Data Project full student population concentrations)

The Homepage shows the data visualization and is interactive. To create the data visualization, we used Charts.js which
is a JavaScript library used to create charts and other data visualization. We have two donut charts: the one on the left has every concentration and the
number of students committed to that concentration. The donut chart on the right is the same thing but for student-athletes.
Our other chart is a multi-line graph, with the ability to select any department. When a department is selected, the distribution
of coursetimes (start times) for that department are displayed on the graph below. Any number of departments can be selected at
a given time. It is most useful, however, when viewing 1-2 departments at a time and noting their respective distributions.
Occasionally, the JavaScript glitches and either the colors are not uniform between charts, or one of the graphs is grey. If this
happens, please refresh the page.

To obtain the data, we used a data scraping algorithm to go through each athletic website and retrieve the concentration data
for each athlete on each team. We also used a data scraping algorithm to get data for every course time from the registar.
Please read more about these implementation details in our "DESIGN.md" file.

We believe that this data can be very useful for the Harvard Athletic department in understanding the disparity between
athletes and non-athletes at Harvard, so we plan on continuing our work on this concept during J-term and presenting
our work to the athletic department.


Our final presentation can be seen at: https://www.youtube.com/watch?v=y_JjeK6I0P8&feature=youtu.be



Resources:

Concentration data taken from Harvard Open Data Project. Link: https://github.com/Harvard-Open-Data-Project/harvard-data/blob/master/concentrations-and-class-enrollment/Concentration%20Data.csv

HTML/Flask Skeleton taken from CS50 Finance.

Used Charts.js and modified it to have a more viewer friendly legend.

Randomized color functions borrowed from https://stackoverflow.com/questions/45771849/chartjs-random-colors-for-each-part-of-pie-chart-with-data-dynamically-from-data
