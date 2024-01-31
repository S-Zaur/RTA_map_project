import joblib
import xgboost as xgb
import pandas as pd
import numpy as np
import json

from urllib import parse
from django.http import JsonResponse
from django.shortcuts import render
from .DatabaseAPI import DatabaseApi
from .prm_values import (
    all_params,
    rta_prm_names,
    vehicle_prm_names,
    params_for_prediction,
)

db = DatabaseApi()


def index(request):
    map_path = "./static/files/map.json"
    with open(map_path, encoding="utf-8") as file:
        map_data = json.load(file)

    return render(
        request, "index.html", {"map_data": map_data, "long_prms": all_params}
    )


def update_params(request):
    jsn_parameters = json.loads(request.headers["Parameters"])
    percentage_mode = request.headers["Percentageresult"]

    appear_keys = jsn_parameters["keys"]
    appear_values = [[parse.unquote(j) for j in i] for i in jsn_parameters["values"]]

    rta_keys, rta_vals = appear_keys.copy(), appear_values
    vehicle_keys, vehicle_vals = [], []
    participant_keys, participant_vals = [], []

    for key in appear_keys:
        if key in rta_prm_names:
            continue
        ind = rta_keys.index(key)

        if key not in vehicle_prm_names:
            participant_keys.append(rta_keys[ind][14:])
            participant_vals.append(rta_vals[ind])
        else:
            vehicle_keys.append(rta_keys[ind][10:])
            vehicle_vals.append(rta_vals[ind])

        del rta_keys[ind]
        del rta_vals[ind]

    js_data = db.select(
        (rta_keys, rta_vals) if len(rta_keys) > 0 else None,
        (vehicle_keys, vehicle_vals) if len(vehicle_keys) > 0 else None,
        (participant_keys, participant_vals) if len(participant_keys) > 0 else None,
    )

    if percentage_mode == "true":
        js_data = db.as_percentage(js_data)

    return JsonResponse({"my_data": js_data})


def prediction(request):
    return render(
        request, "prediction.html", {"params_for_prediction": params_for_prediction}
    )


def prediction_update_params(request):
    jsn_parameters = json.loads(request.headers["Parameters"])

    appear_keys = jsn_parameters["keys"]
    appear_values = [[parse.unquote(j) for j in i] for i in jsn_parameters["values"]]

    if not appear_keys:
        js_data = "Выберите параметры!"
        return JsonResponse({"prediction": js_data})
    key_to_label = {"light": 0, "weather": 1, "brand": 2, "color": 3, "gender": 4}
    labeler_file_name = "Labels_every4_v2.pkl"
    labeler = joblib.load(labeler_file_name)

    for i in range(len(appear_keys)):
        if appear_keys[i] in key_to_label.keys():
            appear_values[i] = labeler[key_to_label[appear_keys[i]]].transform(
                appear_values[i]
            )

    df = pd.DataFrame(data=np.array(appear_values).T, columns=appear_keys)
    df = df[
        ["light", "weather", "experience", "brand", "color", "gender", "year"]
    ].astype(int)

    predictor_file_name = "XGBClassifier_new.json"
    predictor = xgb.Booster()
    predictor.load_model(predictor_file_name)
    predictor_answer = predictor.predict(xgb.DMatrix(df))

    ans_to_str = ["лёгкой тяжести", "с погибшими", "тяжёлым"]
    final_answer = ans_to_str[predictor_answer.argmax()]

    js_data = "Если вы попадёте в ДТП, то скорее всего оно будет " + final_answer

    return JsonResponse({"prediction": js_data})


def about_project(request):
    return render(request, "about_project.html")


def about_us(request):
    return render(request, "about_us.html")


def analytics(request):
    return render(request, "analytics.html")
