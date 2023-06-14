from django.urls import path, include, re_path
from django.views.generic import TemplateView
from events.views import EventListCreateApiView,EventRetrieveUpdateDestroyAPIView,AdminEventListCreateApiView

urlpatterns = [
      path('', EventListCreateApiView.as_view(),name=''),
      path('admin/', AdminEventListCreateApiView.as_view(),name=''),
      path('<int:pk>', EventRetrieveUpdateDestroyAPIView.as_view(),name=''),
]
