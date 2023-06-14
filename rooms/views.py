from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rooms.models import Room
from rooms.serializers import RoomSerializer
from django.shortcuts import get_object_or_404

class RoomListCreateApiView(ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    
class RoomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
   
