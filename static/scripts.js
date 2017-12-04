$(document).ready(function() {
    $.getJSON("/coursetimes", function(json) {
        console.log(json);
        new Chart(document.getElementById("lineChart"), {
            type: 'line',
            data: {
                labels: [1,2,3,4,5,6],
                datasets: [{
                    label: '# of Courses',
                    data: [12, 19, 3, 5, 2, 3],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
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

        var myDoughnutChart = new Chart(document.getElementById("studentPieChart"), {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [10, 20, 30],
                    backgroundColor: ['rgba(255, 99, 132, 0.8)', 'rgba(54, 162, 235, 0.8)', 'rgba(255, 206, 86, 0.8)']
                }],
                labels: ['red', 'yellow', 'blue'],
            },
        });

        var myDoughnutChart = new Chart(document.getElementById("athletePieChart"), {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [10, 20, 30],
                    backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)']
                }],
                labels: ['red', 'yellow', 'blue'],
            },
        });
    });
})