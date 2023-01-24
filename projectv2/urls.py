"""projectv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
    path('admin/', admin.site.urls),
]
