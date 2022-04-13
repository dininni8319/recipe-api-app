
from rest_framework.generics import GenericAPIView
from .serializers import LunchGroupSerializer
from .models import LunchGroup
from rest_framework.response import Response
from rest_framework import status

#the views files contains the necessery logic for the API
class LunchEventAPIView(GenericAPIView):
    """Create a new Event into the db"""

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            serializer_class = LunchGroupSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
                