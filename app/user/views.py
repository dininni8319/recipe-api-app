from rest_framework import generics #module
from rest_framework.authtoken.views import ObtainAuthToken # this comes with django  
from rest_framework.settings import api_settings

from .serializer import UserSerializer, AuthTokenSerializer 

class CreateUserView(generics.CreateAPIView):  
    """Create a new user in the system"""
    serializer_class = UserSerializer #class variable that points to the Serializer class


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES 