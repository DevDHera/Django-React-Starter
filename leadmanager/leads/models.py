"""This used to specify the model for the project"""
from django.db import models


class Lead(models.Model):
    """Configure the Lead Model"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
