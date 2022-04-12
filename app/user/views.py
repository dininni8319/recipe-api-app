from rest_framework import generics #module

from user.serializers import UserSerializer 

class CreateUserView(generics.CreateApiView):  
    """Create a new user in the system"""
    serializer_class = UserSerializer #class variable that points to the Serializer class
