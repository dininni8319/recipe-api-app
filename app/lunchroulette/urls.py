from django.urls import path
from .views import LunchEventAPIView

urlpatterns = [
    path('', LunchEventAPIView.as_view()),
    path('<int:id>', LunchEventAPIView.as_view()),
]