//  -------------------------  FUNCTIONS  -------------------------  //

function showHidePanel() {
    document.getElementById('myDropdown').classList.toggle('show');
}

function screenScaleUpdate() {
    width = document.body.clientWidth;
    height = width * aspectRatio;

    mapSvg.attr('width', width).attr('height', height)
    projection.scale(1400 * width / 1920).translate([width / 2, height / 2]);
}

function parametersListenersSet(parameters) {
    all_prms = [...Object.keys(parameters)]

    all_prms.forEach(function(x) {
        var el = '.' + x
        console.log(el, el + '_menu');
        $(el).on('click', function () {
            $(el + '_menu').toggleClass('show_colour');
        })
    })
}

function requestData() {
    const url = 'update_params';

    const colorCheckedBoxes = Array.from(document.querySelectorAll('input[name=checkbox_color]:checked'), ({value}) => encodeURIComponent(value));
    const severityCheckedBoxes = Array.from(document.querySelectorAll('input[name=checkbox_severity]:checked'), ({value}) => encodeURIComponent(value));
    const participantCheckedBoxes = Array.from(document.querySelectorAll('input[name=checkbox_participant]:checked'), ({value}) => encodeURIComponent(value));
    const genderCheckedBoxes = Array.from(document.querySelectorAll('input[name=checkbox_gender]:checked'), ({value}) => encodeURIComponent(value));
    const lightCheckedBoxes = Array.from(document.querySelectorAll('input[name=checkbox_light]:checked'), ({value}) => encodeURIComponent(value));
    const dateRange = Array.from(document.querySelectorAll('input[name=date_dtp]'), ({value}) => value);

    const percentageMode = document.querySelector('input[id=checkbox_percentage]').checked;
    const tableUsed = document.querySelector('input[name=radio_table]:checked').value;
    lastResultInPercentage = percentageMode;
    console.log(tableUsed)
    var keys = [], values = [];

    if (colorCheckedBoxes.length > 0) { keys.push('vehicles__color'); values.push(colorCheckedBoxes); }  // !!!
    if (severityCheckedBoxes.length > 0) { keys.push('severity'); values.push(severityCheckedBoxes); }
    if (participantCheckedBoxes.length > 0) { keys.push('participant_categories'); values.push(participantCheckedBoxes); }
    if (genderCheckedBoxes.length > 0) { keys.push('participants__gender'); values.push(genderCheckedBoxes); }  // !!!
    if (lightCheckedBoxes.length > 0) { keys.push('light'); values.push(lightCheckedBoxes); }
    if (dateRange[0] != '' && dateRange[1] != '') { keys.push('rta_date'); values.push(dateRange); }

    all_prms.forEach(function(prm_name) {
        const checkedBoxes = Array.from(document.querySelectorAll('input[name=checkbox_' + prm_name + ']:checked'), ({value}) => encodeURIComponent(value));
        if (checkedBoxes.length > 0) { keys.push(prm_name); values.push(checkedBoxes); }
    })

    const parametersString = JSON.stringify({'keys': keys, 'values': values});
    console.log(parametersString);

    fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Parameters': parametersString,
            'Percentageresult': percentageMode,
            'Tableused': tableUsed,
        },
    })
        .then(response => {
            return response.json();
        })
        .then(data => {
            regionData = data['my_data']

            regionDataArr = Object.values(regionData)

            let maxV = Math.max(...regionDataArr)
            let minV = Math.min(...regionDataArr)
            let delta = maxV - minV

            colorDomain = [minV + delta * 0.2, minV + delta * 0.4, minV + delta * 0.6, minV + delta * 0.8, minV + delta]
            paint = d3.scale.threshold().domain(colorDomain).range(mapColors);
            console.log('norm')
            mapRedraw(regionData);
        })
}

function mapRedraw(data) {
    var regionValues = {};
    for (var key in data) {
        regionValues[key] = +data[key];
    }

    mapSvg.selectAll("*").remove();

    mapSvg.append('g')
        .attr('class', 'region')
        .selectAll('path')
        .data(topojson.object(mapJson, mapJson.objects.russia).geometries)
        .enter().append('path')
        .attr('d', path)
        .style('fill', function (d) {
            if (d.properties.region in regionValues)
                return paint(regionValues[d.properties.region]);
            return nanColor;
        })
        .style('opacity', 0.8)

        //  Mouse Events
        .on('mouseover', function (d) {
            d3.select(this).transition().duration(300).style('opacity', 1);
            tooltipDiv.transition().duration(300).style('opacity', 1);
            tooltipDiv.text(d.properties.region + ' : ' + regionValues[d.properties.region])
                .style('left', (d3.event.pageX) + 'px')
                .style('top', (d3.event.pageY - 30) + 'px');

            if (lastResultInPercentage)
                tooltipDiv.text(d.properties.region + ' : ' + regionValues[d.properties.region] + '%')
        })

        .on('mouseout', function () {
            d3.select(this).transition().duration(300).style('opacity', 0.8);
            tooltipDiv.transition().duration(300).style('opacity', 0);
        })
};

//  -------------------------  SOME IMPORTANT VARIABLES  -------------------------  //

const aspectRatio = 9 / 16;
var width = document.body.clientWidth;
var height = width * aspectRatio;

const mapColors = ['#3FFF3F', '#84FF32', '#D3FF26', '#FFD119', '#FF6D0C', '#FF0000'];
const nanColor = '#BFBFBF'

var regionData;
var lastResultInPercentage = false;

//  -------------------------  LISTENERS  -------------------------  //

window.addEventListener('resize', function(event) {
    screenScaleUpdate();
    mapRedraw(regionData);
})

$(".color").on("click", function () {
    $(".color_menu").toggleClass("show_colour");
})
$(".severity").on("click", function () {
    $(".severity_menu").toggleClass("show_severity");
})
$(".participant").on("click", function () {
    $(".participant_category_menu").toggleClass("show_participant");
})
$(".gender_").on("click", function () {
    $(".gender_menu").toggleClass("show_gender");
})
$(".light").on("click", function () {
    $(".light_menu").toggleClass("show_light");
})

//  -------------------------  CONTAINERS  -------------------------  //

var mapSvg = d3.select('body').append('svg')
    .attr('width', width)
    .attr('height', height)
    .style('margin', '10px auto');

var projection = d3.geo.albers()
    .rotate([-105, 0])
    .center([-10, 65])
    .parallels([52, 64])
    .scale(900)
    .translate([width / 2, height / 2]);

var path = d3.geo.path().projection(projection);

var tooltipDiv = d3.select('body').append('div')
    .attr('class', 'tooltip')
    .style('opacity', 0);

/*
var legend = mapSvg.selectAll("g.legend")
    .data(ext_color_domain)
    .enter().append("g")
    .attr("class", "legend");

var ls_w = 20, ls_h = 20;

legend.append("rect")
    .attr("x", 20)
    .attr("y", function (d, i) {
        return height - (i * ls_h) - 2 * ls_h;
    })
    .attr("width", ls_w)
    .attr("height", ls_h)
    .style("fill", function (d, i) {
        return paint(d);
    })
    .style("opacity", 0.8);

legend.append("text")
    .attr("x", 50)
    .attr("y", function (d, i) {
        return height - (i * ls_h) - ls_h - 4;
    })
    .text(function (d, i) {
        return legend_labels[i];
    });
*/

//  -------------------------  EVERYTHING ELSE  -------------------------  //