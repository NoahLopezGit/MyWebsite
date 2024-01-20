const events_in_progress = ['time', 'temp', 'pressure'];
function lepotato_display_updateAllEvents() {
    //events_in_progress is a list of endpoints with event data   
    // events_in_progress.forEach(function (event_endpoint, index) {
    //     $.get(event_endpoint, function (data, status) {
    //         updateEvent(data);
    //     });
    // });
    events_in_progress.forEach(function (event_endpoint) {
        fetch('/API/lepotato-display/' + event_endpoint)
            .then((server_response) => server_response.json())
            .then((json_obj) => updateEvent(json_obj, event_endpoint))
    })
}

function updateEvent(json_obj, event_endpoint) {
    document.getElementById(event_endpoint).innerHTML = json_obj[event_endpoint]
    // var event_tile_id = data.sport + “-” + data.id;
    // var away_score = document.getElementById(event_tile_id + “-away - score”);
    // var home_score = document.getElementById(event_tile_id + “-home - score”);
    // if (away_score && home_score) {
    //     away_score.innerHTML = new_data.away_score;
    //     home_score.innerHTML = new_data.home_score;
    // }
}