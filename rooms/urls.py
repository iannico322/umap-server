from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rooms.views import RoomListCreateApiView,RoomRetrieveUpdateDestroyAPIView

urlpatterns = [
      path('', RoomListCreateApiView.as_view(),name=''),
      path('<int:pk>', RoomRetrieveUpdateDestroyAPIView.as_view(),name=''),
]
