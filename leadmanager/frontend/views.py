"""This used to specify the views for the project"""
from django.shortcuts import render


def index(request):
    """Configure the render method"""
    return render(request, 'frontend/index.html')
