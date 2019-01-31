"""This used to specify the urls for the frontend"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)
]
