from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import LunchGroup

class LunchGroupSerializer(serializers.ModelSerializer):
    admin = get_user_model()
    
    class Meta:
        model=LunchGroup
        fields=['name_event', 'description', 'created', 'update', 'number_people']