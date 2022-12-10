import multiprocessing
from urllib import parse

from django.http import JsonResponse
from django.shortcuts import render
from .DatabaseAPI import DatabaseApi, add_stat
import json

from .prm_values import all_params, rta_prm_names, vehicle_prm_names, participant_prm_names

db = DatabaseApi()


def index(request):
    map_path = '.\\static\\files\\map.json'
    with open(map_path, encoding='utf-8') as file:
        map_data = json.load(file)

    return render(request, 'index.html', {'map_data': map_data, 'long_prms': all_params})


def about_project(request):
    return render(request, 'about_project.html')


def about_us(request):
    return render(request, 'about_us.html')


def analytics(request):
    return render(request, 'analytics.html')


def update_params(request):
    jsn_parameters = json.loads(request.headers['Parameters'])
    percentage_mode = request.headers['Percentageresult']
    stat = db.get_stat(jsn_parameters)
    if stat is not None:
        if percentage_mode == 'true':
            stat = db.as_percentage(stat)
        return JsonResponse(stat)

    appear_keys = jsn_parameters['keys']
    appear_values = jsn_parameters['values']
    appear_values = [[parse.unquote(j) for j in i] for i in appear_values]

    rta_keys, rta_vals = appear_keys.copy(), appear_values
    vehicle_keys, vehicle_vals = [], []
    participant_keys, participant_vals = [], []

    for key in appear_keys:
        if key not in rta_prm_names:
            ind = rta_keys.index(key)

            if key not in vehicle_prm_names:
                participant_keys.append(rta_keys[ind][14:])
                participant_vals.append(rta_vals[ind])
            else:
                vehicle_keys.append(rta_keys[ind][10:])
                vehicle_vals.append(rta_vals[ind])

            del rta_keys[ind]
            del rta_vals[ind]

    js_data = db.select((rta_keys, rta_vals) if len(rta_keys) > 0 else None,
                        (vehicle_keys, vehicle_vals) if len(vehicle_keys) > 0 else None,
                        (participant_keys, participant_vals) if len(participant_keys) > 0 else None)

    if percentage_mode == 'true':
        js_data = db.as_percentage(js_data)

    data = {'my_data': js_data}

    process = multiprocessing.Process(target=add_stat, args=(jsn_parameters, data))
    process.start()

    return JsonResponse(data)
