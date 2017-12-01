var academicYear;
var years = ["2010","2011","2012","2013","2014"];
var timeSeriesChart

var colorLightest = "#3DC3CC";
var colorLight = "#00BFCC";
var colorMedium = "#2D8E95";
var colorDark = "#00777F";
var colorDarkest = "#00484C";


window.onload = function() {
    var y2010 = $("#2010");
    var y2011 = $("#2011");
    var y2012 = $("#2012");
    var y2013 = $("#2013");
    var y2014 = $("#2014");

    var yearTriggers = [y2010, y2011, y2012, y2013, y2014]

    yearTriggers.forEach(function(yearTrigger){
        yearTrigger.click(function(){
            var academicYear = yearTrigger.text();
            if (timeSeriesChart != null) {
                timeSeriesChart.academicYear = academicYear;
                timeSeriesChart.updateVis();
            }
            return false;
        });
    })

    $(".btn-group > a").click(function(){
        $(this).addClass("active");
        $(this).siblings().removeClass("active");
    });
}

function loadData() {
    d3.queue()
        .defer(d3.csv, "data/DegreeData.csv")
        .await(function(error, _dataDegreeData){
            if (error) { console.error('Something went wrong: ' + error); }
            else {
                createVis();
            }
        })
}

function createVis() {
    timeSeriesChart = new TimeSeriesChart("timeSeriesDegreeData", DegreeData.csv);
		updateVis();
}

function updateVis() {
		timeSeriesChart.updateVis();
}


$(".scrollToB").click(function() {
    $('html,body').animate({
        scrollTop: $("#B").offset().top},'slow');
});