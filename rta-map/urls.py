from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('update_params/', views.update_params),
    path('prediction/', views.prediction),
    path('prediction_update_params/', views.prediction_update_params),
    path('about_project/', views.about_project),
    path('about_us/', views.about_us),
    path('analytics/', views.analytics),
]
