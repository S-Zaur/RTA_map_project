from urllib import parse

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .DatabaseAPI import DatabaseApi
import json


def index(request):
    path = '.\\static\\files\\map.json'
    with open(path) as f:
        map_data = json.load(f)

    db = DatabaseApi()
    js_data = db.select_count_rta_by_region()

    return render(request, 'index.html', {'my_data': js_data, 'map_data': map_data})


def ajax_get_view(request):  # May include more arguments depending on URL parameters
    jsn = json.loads(request.headers['Prms'])
    b = jsn['prm_0']
    a = jsn['prm_1']

    a = [parse.unquote(i) for i in a]
    db = DatabaseApi()
    js_data = db.as_percentage(db.select_count_rta_by_key_values(parse.unquote(jsn['prm_0']), a))
    data = {'my_data': js_data}
    return JsonResponse(data)
