from django.urls import path

from schedules.views import schedules_by_user,ScheduleRetrieveUpdateDestroyAPIView,ScheduleListCreateApiView
from . import views
urlpatterns = [
      path('', ScheduleListCreateApiView.as_view(),name=''),
      path('<int:pk>', ScheduleRetrieveUpdateDestroyAPIView.as_view(),name=''),
      path('user/<str:userID>', views.schedules_by_user),
]
