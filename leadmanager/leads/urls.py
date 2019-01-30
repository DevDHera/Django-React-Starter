"""This used to specify the serializer for the project"""
from rest_framework import routers
from .api import LeadViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register('api/leads', LeadViewSet, 'leads')

urlpatterns = ROUTER.urls
