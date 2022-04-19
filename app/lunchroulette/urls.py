from django.urls import path
from .views import LunchEventAPIView, ListPlacesAPIView, ParticipantsAPIView, RandomUserAPIView

urlpatterns = [
    path('create_event', LunchEventAPIView.as_view()),
    path('random_event', RandomUserAPIView.as_view()),
    path('add_restaurant', ListPlacesAPIView.as_view()),
    path('add_partecipant', ParticipantsAPIView.as_view()),
    path('<int:id>', LunchEventAPIView.as_view()),
]