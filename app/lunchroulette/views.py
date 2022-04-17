
from rest_framework.generics import GenericAPIView
from .serializers import LunchGroupSerializer, EventParticipantsSerializer, ListPlacesSerializer
from .models import LunchGroup
from rest_framework.response import Response
from rest_framework import status

#the views files contains the necessery logic for the API
class LunchEventAPIView(GenericAPIView):

    def get(self, request, id=None):
        """Get all lunch events planned for the week"""
        
        lunch_event = LunchGroup.objects.all()

        if request.method == 'GET':
            if id:
                lunch_event = LunchGroup.objects.get(id=id)
                lunch_serializer = LunchGroupSerializer(lunch_event)
                return Response({"data":lunch_serializer.data, "status": 'success'}, status=status.HTTP_201_CREATED)
            
            lunch_serializer = LunchGroupSerializer(lunch_event, many=True)

            return Response({"data":lunch_serializer.data, "status": 'success'}, status=status.HTTP_201_CREATED)
        
        return Response(lunch_event.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, *args, **kwargs):
        """Create a new Event into the db"""

        if request.method == "POST":
            serializer_class = LunchGroupSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPlacesAPIView(GenericAPIView):  
    """Add a place to the list where we could have lunch"""   
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer_class = ListPlacesSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        """Create a list of places where the team could have a lunch"""

                