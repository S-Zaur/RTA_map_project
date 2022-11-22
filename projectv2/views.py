from urllib import parse

from django.http import JsonResponse
from django.shortcuts import render
from .DatabaseAPI import DatabaseApi
import json

from .prm_values import all_params, rta_params, vehicles_params, participants_params


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
    table_used = request.headers['Tableused']

    # Можно переместить на после выкидывания параметров v v v
    keys = jsn_parameters['keys']  # ['severity', 'light', 'date', ...]
    values = jsn_parameters['values']
    # [['Легкий', 'С погибшими'], ['В темное время суток, освещение включено'], ['2022-10-18', '2022-10-20'], ...]
    values = [[parse.unquote(j) for j in i] for i in values]

    print(table_used)
    print(keys)
    print(values)
    print('^ ^ ^ OLD/NEW v v v')

    db = DatabaseApi()

    match table_used:  # Выброс ненужных параметров
        case 'Vehicles':
            include_arr = vehicles_params
            keys = [key[10:] for key in keys]
            print('vehicles_params')
        case 'Participants':
            include_arr = participants_params
            keys = [key[14:] for key in keys]
            print('participants_params')
        case _:
            include_arr = rta_params
            print('rta_params')

    appear_keys = keys.copy()
    for key in appear_keys:
        print(key, 'in', include_arr)
        if key not in include_arr:
            ind = keys.index(key)
            print(ind)
            del keys[ind]
            del values[ind]

    print(keys)
    print(values)

    match table_used:  # Выброс ненужных параметров
        case 'Vehicles':
            js_data = db.select_count_vehicles(keys, values)
        case 'Participants':
            js_data = db.select_count_participants(keys, values)
        case _:
            js_data = db.select_count_rta_by_keys_values(keys, values)
    if percentage_mode == 'true':
        js_data = db.as_percentage(js_data)

    data = {'my_data': js_data}
    print(data)
    return JsonResponse(data)
