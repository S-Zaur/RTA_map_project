//  -------------------------  FUNCTIONS  -------------------------  //

function getRandomInt(max) {
    max = Math.floor(max);
    return Math.floor(Math.random() * (max + 1));
}

function requestData(number) {
    var url = 'update_params';
    var prm_0 = number;
    var prm_1 = number;

    console.log(prm_0);
    console.log(prm_1);
    var prmstring = JSON.stringify({"prm_0" : prm_0, "prm_1" : prm_1 })

    fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Prms': prmstring,
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    .then(response => {
        //console.log('got something');
        return response.json();
    })
    .then(data => {
        //  REDRAW MAP
        mapRedraw(mapJson, data['my_data']);
    })
}

function mapRedraw(map, data) {
	var regionValues = {};
	//console.log(typeof data);
	//console.log(data);

	for (var key in data) {
	    //console.log(key)
		regionValues[key] = +data[key];
	}

	//  TODO colors max min

	//console.log(region_values);

	//  Drawing Russia with cpoetry run python manage.py runserverolors

    mapSvg.selectAll("*").remove();

	mapSvg.append("g")
	.attr("class", "region")
	.selectAll("path")
	.data(topojson.object(map, map.objects.russia).geometries)
	.enter().append("path")
	.attr("d", path)
	.style("fill", function(d) {
		return paint(regionValues[d.properties.region]);
	})
	.style("opacity", 0.8)  //  connect

	///*  //  mouse things
	.on("mouseover", function(d) {
        d3.select(this).transition().duration(300).style("opacity", 1);
        tooltipDiv.transition().duration(300)
        .style("opacity", 1)
        //tooltipDiv.text(nameById[d.properties.region] + " : " + rateById[d.properties.region])
        tooltipDiv.text("" + " : " + regionValues[d.properties.region])
        .style("left", (d3.event.pageX) + "px")
        .style("top", (d3.event.pageY -30) + "px");
    })
    .on("mouseout", function() {
        d3.select(this)
        .transition().duration(300)
        .style("opacity", 0.8);
        tooltipDiv.transition().duration(300)
        .style("opacity", 0);
    })
    //*/

    /*  //  points
    d3.tsv("cities.tsv", function(error, data) {
        var city = svg.selectAll("g.city")
        .data(data)
        .enter()
        .append("g")
        .attr("class", "city")
        .attr("transform", function(d) { return "translate(" + projection([d.lon, d.lat]) + ")"; });

        city.append("circle")
        .attr("r", 3)
        .style("fill", "lime")
        .style("opacity", 0.75);

        city.append("text")
        .attr("x", 5)
        .text(function(d) { return d.City; });
    });
    */
};

//  -------------------------  SOME IMPORTANT VARIABLES  -------------------------  //

var width = document.documentElement.scrollWidth, height = 768;  //  960 500

var color_domain = [50, 150, 350, 750, 1500]
var ext_color_domain = [0, 50, 150, 350, 750, 1500]
var legend_labels = ["< 50", "50+", "150+", "350+", "750+", "> 1500"]  //  will be changed for percentage ig
var paint = d3.scale.threshold()
.domain(color_domain)
.range(["#7FFF7F", "#92E55B", "#AFCC3D", "#B29523", "#99460F", "#7F0000"]);

//  -------------------------  CONTAINERS  -------------------------  //

var mapSvg = d3.select("body").append("svg")
.attr("width", width)
.attr("height", height)
.style("margin", "10px auto");

var projection = d3.geo.albers()
.rotate([-105, 0])
.center([-10, 65])
.parallels([52, 64])
.scale(900)
.translate([width / 2, height / 2]);

var path = d3.geo.path().projection(projection);

var tooltipDiv = d3.select("body").append("div")
.attr("class", "tooltip")               
.style("opacity", 0);

var legend = mapSvg.selectAll("g.legend")
.data(ext_color_domain)
.enter().append("g")
.attr("class", "legend");

var ls_w = 20, ls_h = 20;

legend.append("rect")
.attr("x", 20)
.attr("y", function(d, i) { return height - (i * ls_h) - 2 * ls_h; } )
.attr("width", ls_w)
.attr("height", ls_h)
.style("fill", function(d, i) { return paint(d); })
.style("opacity", 0.8);

legend.append("text")
.attr("x", 50)
.attr("y", function(d, i) { return height - (i * ls_h) - ls_h - 4; } )
.text(function(d, i) { return legend_labels[i]; } );

//  -------------------------  EVERYTHING ELSE  -------------------------  //