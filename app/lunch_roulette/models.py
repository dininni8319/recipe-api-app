from django.contrib.auth import get_user_model
from turtle import update
from venv import create
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class LunchGroup(models.Models):

    name_event = models.CharField(max_length=100)

    description = models.TextField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    
    update = models.DateTimeField(auto_now=True)

    admin = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='lunch_group'
    )

    number_people = models.IntegerField(
        default=1,
        validators=[
           MaxValueValidator(50),
           MinValueValidator(1) 
        ]
    )
