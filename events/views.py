from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from events.models import Event
from events.serializers import EventSerializer
from django.utils import timezone

class AdminEventListCreateApiView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventListCreateApiView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(date__gte=timezone.now()).order_by('date')

    
class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
   