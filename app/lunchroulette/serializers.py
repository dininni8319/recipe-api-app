from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import LunchGroup, Partecipat, ListPlace

class LunchGroupSerializer(serializers.ModelSerializer):
    admin = get_user_model()
    
    class Meta:
        model = LunchGroup
        fields = ['name_event', 'description', 'created', 'update', 'number_people']

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partecipat
        fields = ['name_partecipant']

class ListPlacesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ListPlace
        fields = ['restaurant_name']
