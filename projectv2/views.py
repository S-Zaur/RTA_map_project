from urllib import parse

from django.http import JsonResponse
from django.shortcuts import render
from .DatabaseAPI import DatabaseApi
import json

db = DatabaseApi()


def index(request):
    map_path = '.\\static\\files\\map.json'
    with open(map_path, encoding='utf-8') as file:
        map_data = json.load(file)

    return render(request, 'index.html', {'map_data': map_data})


def about_project(request):
    return render(request, 'about_project.html')


def about_us(request):
    return render(request, 'about_us.html')


def analytics(request):
    return render(request, 'analytics.html')


def update_params(request):
    jsn_parameters = json.loads(request.headers['Parameters'])
    percentage_mode = request.headers['Percentageresult']

    keys = jsn_parameters['keys']  # ['severity', 'light', 'date', ...]
    values = jsn_parameters[
        'values']  # [['Легкий', 'С погибшими'], ['В темное время суток, освещение включено'], ['2022-10-18', '2022-10-20'], ...]
    values = [[parse.unquote(j) for j in i] for i in values]

    print(keys)
    print(values)

    if not keys:
        js_data = db.select_count_rta_by_region()
    elif percentage_mode == 'true':
        js_data = db.as_percentage(db.select_count_rta_by_keys_values(keys, values))
    else:
        js_data = db.select_count_rta_by_keys_values(keys, values)

    data = {'my_data': js_data}
    return JsonResponse(data)
