from django.conf import settings

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class LunchGroup(models.Model):

    name_event = models.CharField(
        verbose_name='name_event',
        max_length=100
    )

    description = models.TextField(
        verbose_name='description',
        max_length=1000,
        blank=True,
    )

    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )
    
    update = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='update',
    )

    admin = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='admin_id',
        null=True
    )

    number_people = models.IntegerField(
        default=1,
        validators=[
           MaxValueValidator(8),
           MinValueValidator(1) 
        ],
        blank=True
    )

    # class Meta: 
    #     db_table="lunchroulette"
        
    def __str__(self):
        name_event = f'{self.name_event[:30]}...' if len(self.name_event) > 30 else self.name_event
        return f' {self.pk}: {name_event}'

class EventPartecipats(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True
    )
