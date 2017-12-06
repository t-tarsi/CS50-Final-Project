$(document).ready(function() {
    // Establish color array so that our 2 donut charts will be include the same colors
    var colors = [];

    // randomized color functions borrowed from https://stackoverflow.com/questions/45771849/chartjs-random-colors-for-each-part-of-pie-chart-with-data-dynamically-from-data
    // Altered to establish the 4th parameter, t, which is the transparency
    var dynamicColors = function(t) {
        var r = Math.floor(Math.random() * 255);
        var g = Math.floor(Math.random() * 255);
        var b = Math.floor(Math.random() * 255);

        return "rgba(" + r + "," + g + "," + b + "," + t + ")";
    };

    var getColors = function(n, t) {
        color_info = []
        for (var i = 0; i < n; i++) {
            color_info.push(dynamicColors(t))
        }
        return color_info;
    }

    // Get JSON data from the concentrations route, which has the concentration data for all Harvard students
    $.getJSON("/concentrations", function(data) {

        // Get randomized colors from the function, with a transparency parameter of 0.8. This data will be used for the second donut chart as well.
        color_info = getColors(Object.keys(data).length, "0.8");

        // Define donut chart, grabbing the necessary html element
        var myDoughnutChart = new Chart(document.getElementById("studentPieChart"), {
            type: 'doughnut',

            // Use the values from the json data for the values in the chart
            data: {
                datasets: [{
                    data: Object.values(data),
                    backgroundColor: color_info
                }],

                // Use the keys from the json data as the labels on our chart
                labels: Object.keys(data)
                },

                // Edit some options
            options: {
                legend: {
                    display: false,
                },
                responsive: true,
                title: {
                    display: true,
                    text:'Student Concentrations',
                    fontSize: 20
                },
            }
        });
    });


    // Get JSON data from the /AthleteConcentrations route, which has the concentration data for Harvard student-athletes
    $.getJSON("/AthleteConcentrations", function(data) {

        // Define donut chart, grabbing the necessary html element
        var myDoughnutChart = new Chart(document.getElementById("athletePieChart"), {
            type: 'doughnut',

            // Use the values from the json data for the values in the chart
            data: {
                datasets: [{
                    data: Object.values(data),

                    // Use the color data from the previous chart for this one as well, to maintain uniformity
                    backgroundColor: color_info
                }],

                // Use the keys from the json data as the labels on our chart
                labels: Object.keys(data),
            },

            // Edit some options
            options: {
                legend: {
                    display: false
                },
                responsive: true,
                title: {
                    display: true,
                    text:'Athlete Concentrations',
                    fontSize: 20
                }
            }
        });
    })

    // Get JSON data from the coursetimes route, which has each department's distribution of coursetimes
    $.getJSON("/coursetimes", function(data) {

        // Necessary because of the weird format of the data
        data=data[0]

        // Create datalist that will be used as our data object
        dataList = []

        // For every department, we need to establish a value in the dataList
        for (var key in data) {
            dataList.push({
                label: key,
                data: Object.values(data[key]),
                backgroundColor: getColors(1, "0.4")[0], hidden: true
            })
        }

        // Define new chart using necessary html element
        new Chart(document.getElementById("lineChart"), {
            type: 'line',
            data: {
                // Establish the labels as the labels for one department (arbitrary, because they're all the same). We just need to establish some labels
                labels: Object.keys(data["AESTHINT"]),

                // Implement our dataList as the dataset
                datasets: dataList
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    });

})