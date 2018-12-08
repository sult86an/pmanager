
<!-- Chart code -->

var chart = AmCharts.makeChart( "chartdiv", {
"type": "serial",
"theme": "light",
"dataProvider": [ {
"country": "الأولى",
"visits": 66
}, {
"country": "الثانية",
"visits": 44
}, {
"country": "الثالثة",
"visits": 100
}, {
"country": "الرابعة",
"visits": 90
}, {
"country": "الخامسة",
"visits": 50
}, {
"country": "السادسة",
"visits": 80
}, {
"country": "السابعة",
"visits": 70
}, {
"country": "الثامنة",
"visits": 60
}, {
"country": "التاسعة",
"visits": 50
}],
"valueAxes": [ {
"gridColor": "#fff",
"gridAlpha": 0.2,
"dashLength": 0
} ],
"gridAboveGraphs": true,
"startDuration": 2,
"graphs": [ {
"balloonText": "[[category]]: <b>[[value]]</b>",
"fillAlphas": 0.8,
"lineAlpha": 0.2,
"type": "column",
"valueField": "visits"
} ],
"chartCursor": {
"categoryBalloonEnabled": false,
"cursorAlpha": 0,
"zoomable": false
},
"categoryField": "country",
"categoryAxis": {
"gridPosition": "start",
"gridAlpha": 0,
"tickPosition": "start",
"tickLength": 20
},
"export": {
"enabled": false
}

} );
