var answer = "";

//  -------------------------  FUNCTIONS  -------------------------  //

function parametersListenersSet(parameters) {
    $('.dropbtn').on('click', function () {
        $('#dropdown').toggleClass('show');
    })

    $('.color_span_menu').on('click', function () {
        $('.color_menu').toggleClass('show_colour');
    })

    $('.gender_span_menu').on('click', function () {
        $('.gender_menu').toggleClass('show_gender');
    })

    all_prms = [...Object.keys(parameters)]

    all_prms.forEach(function (prm_name) {
        var el = '.' + prm_name
        console.log(el, el + '_menu');
        $(el + '_span_menu').on('click', function () {
            $(el + '_menu').toggleClass('hidden_menu');
        })
    })
}

function requestData() {
    const url = '/prediction_update_params';

    var carYearElement = document.querySelector('input[name=year]');
    if (carYearElement.value == '')
        carYearElement.value = '2023';

    var colorCheckedRadios = Array.from(document.querySelectorAll('input[name=radio_color]:checked'), ({ value }) => encodeURIComponent(value));
    var genderCheckedRadios = Array.from(document.querySelectorAll('input[name=radio_gender]:checked'), ({ value }) => encodeURIComponent(value));
    var carYearElements = Array.from(document.querySelectorAll('input[name=year]'), ({ value }) => encodeURIComponent(value));

    var keys = [], values = [];

    if (colorCheckedRadios.length > 0) { keys.push('color'); values.push(colorCheckedRadios); }
    if (genderCheckedRadios.length > 0) { keys.push('gender'); values.push(genderCheckedRadios); }
    if (carYearElements.length > 0) { keys.push('year'); values.push(carYearElements); }

    all_prms.forEach(function (prm_name) {
        const checkedRadios = Array.from(document.querySelectorAll('input[name=radio_' + prm_name + ']:checked'), ({ value }) => encodeURIComponent(value));
        if (checkedRadios.length > 0) { keys.push(prm_name); values.push(checkedRadios); }
    })

    const parametersString = JSON.stringify({ 'keys': keys, 'values': values });
    console.log(parametersString);

    fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Parameters': parametersString,
        },
    })
        .then(response => {
            return response.json();
        })
        .then(data => {
            answer = data['prediction'];
            $('#answer').html(answer);
        })
}
