"""This used to specify the serializer for the project"""
from rest_framework import serializers
from leads.models import Lead

# Lead Serializer


class LeadSerializer(serializers.ModelSerializer):
    """Configure the Lead Serializer"""
    class Meta:
        model = Lead
        fields = '__all__'
