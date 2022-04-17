from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import LunchGroup, EventPartecipats, ListPlaces

class LunchGroupSerializer(serializers.ModelSerializer):
    admin = get_user_model()
    
    class Meta:
        model = LunchGroup
        fields = ['name_event', 'description', 'created', 'update', 'number_people']

class EventParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPartecipats
        fields = ['name']

class ListPlacesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ListPlaces
        fields = ['restaurant_name']
