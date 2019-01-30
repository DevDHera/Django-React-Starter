"""This used to specify the api for the project"""
from rest_framework import viewsets, permissions
from leads.models import Lead
from .serializers import LeadSerializer

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    """Configure the Lead Viewset"""
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
