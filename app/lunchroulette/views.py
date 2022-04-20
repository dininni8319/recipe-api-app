import random
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from .serializers import LunchGroupSerializer, ListPlacesSerializer, ParticipantsSerializer 

from .models import LunchGroup, ListPlace, Partecipat
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
    
    def get(self, request, id=None):
        """Get the list of all the partecipants"""
        
        list_places = ListPlace.objects.all()

        if request.method == 'GET':
            if id:
                list_places = ListPlace.objects.get(id=id)
                list_serializer = ListPlacesSerializer(list_places)
                return Response({"data":list_serializer.data, "status": 'success'}, status=status.HTTP_201_CREATED)
            
            list_serializer = ListPlacesSerializer(list_places,  many=True)

            return Response({"data":list_serializer.data, "status": 'success'}, status=status.HTTP_201_CREATED)
        
        return Response(list_places.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer_class = ListPlacesSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipantsAPIView(GenericAPIView):

    def get(self, request, id=None):
        """Get the list of all the partecipants"""
        
        list_partecipants = Partecipat.objects.all()

        if request.method == 'GET':
            if id:
                list_partecipants = Partecipat.objects.get(id=id)
                partecipants_serializer = ParticipantsSerializer(list_partecipants)
                return Response({"data":partecipants_serializer.data, "status": 'success'}, status=status.HTTP_201_CREATED)
            
            partecipants_serializer = ParticipantsSerializer(list_partecipants,  many=True)

            return Response({"data":partecipants_serializer.data, "status": 'success'}, status=status.HTTP_201_CREATED)
        
        return Response(list_partecipants.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer_class = ParticipantsSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class RandomUserAPIView(ListCreateAPIView):
    
    def get(self, request):
        random_partecipants = Partecipat.objects.all().order_by('?')[:8]
        random_placeses = ListPlace.objects.all().order_by('?')[:8]
        if request.method == 'GET':
            random_partecipants_serializer = ParticipantsSerializer(random_partecipants, many=True)
            random_placeses_serializer = ListPlacesSerializer(random_placeses, many=True)
            
            return Response({"data":random_partecipants_serializer.data,'places_random': random_placeses_serializer.data, "status": "success"}, status=status.HTTP_201_CREATED)
            
    def post(self, request):
        """Get all the random places and random participant"""
        random_partecipants = Partecipat.objects.all().order_by('?')[:8]
        random_place = ListPlace.objects.all().order_by('?')[:1]
        random_place = random_place[0]
        week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        if request.method =="POST":
            LunchGroup.objects.create(
                name_event = request.POST['name_event'],
                description = request.POST['description'],
                week_day = week_day[0],
                random_place = random_place
            )
        
            return Response({"data": 'ok' , "status": 'success'}) 

