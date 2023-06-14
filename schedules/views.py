from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def schedules_by_user(request, userID):
    if request.method == 'GET':
        schedules = Schedule.objects.filter(userID=userID)
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

class ScheduleListCreateApiView(ListCreateAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    
class ScheduleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()