from django.contrib import admin
from .models import LunchGroup, EventPartecipats, ListPlaces

admin.site.register(LunchGroup)
admin.site.register(EventPartecipats)
admin.site.register(ListPlaces)