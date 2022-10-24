from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from . import toyDatabaseAPI
import json

def index(request):
    path = '.\\static\\files\\map.json'
    with open(path) as f:
        map_data = json.load(f)

    db = toyDatabaseAPI.ToyDatabaseApi()
    js_data = db.select_count_rta_by_key_value('key', 0)
    #print(js_data)
    print('wrong one')

    return render(request, 'index.html', { 'my_data': js_data, 'map_data': map_data })

def ajax_get_view(request): # May include more arguments depending on URL parameters
    print('it does happenssssssssssssssssssssssssss')
    print(request.headers)
    print(request.headers['Prms'])
    a = request.headers['Prms']
    a = json.loads(a)
    a = a['prm_0']
    print(a)

    db = toyDatabaseAPI.ToyDatabaseApi()
    js_data = db.select_count_rta_by_key_value('key', int(a))
    data = { 'my_data' : js_data }
    return JsonResponse(data)