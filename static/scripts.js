$(document).ready(function() {

    // TODO: make pie charts the same color

    var colors = [];

    // random color function borrowed from https://stackoverflow.com/questions/45771849/chartjs-random-colors-for-each-part-of-pie-chart-with-data-dynamically-from-data
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


    $.getJSON("/concentrations", function(data) {
        color_info = getColors(Object.keys(data).length, "0.8");
        colors=color_info
        var myDoughnutChart = new Chart(document.getElementById("studentPieChart"), {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: Object.values(data),
                    backgroundColor: colors
                }],
                labels: Object.keys(data)
                },
            options: {
                legend: {
                    display: true,
                    position: "bottom"
                }
            }
        });
    });

    $.getJSON("/AthleteConcentrations", function(data) {
        color_info = colors;
        var myDoughnutChart = new Chart(document.getElementById("athletePieChart"), {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: Object.values(data),
                    backgroundColor: color_info
                }],
                labels: Object.keys(data),
            },
            options: {
                legend: {
                    display: true,
                    position: "bottom"
                }
            }
        });
    })


    $.getJSON("/coursetimes", function(data) {
        data=data[0]
        dataList = []
        for (var key in data) {
            dataList.push({label: key, data: Object.values(data[key]), backgroundColor: getColors(1, "0.2")[0], hidden: true})
        }
        console.log(dataList)
        new Chart(document.getElementById("lineChart"), {
            type: 'line',
            data: {
                labels: Object.keys(data["AESTHINT"]),
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