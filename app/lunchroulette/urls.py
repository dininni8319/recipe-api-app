from django.urls import path
from .views import LunchEventAPIView

urlpatterns = [
    path('', LunchEventAPIView.as_view()),
]