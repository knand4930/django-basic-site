from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('/logins', views.logins, name='logins'),

]
