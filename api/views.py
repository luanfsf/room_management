from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics

from api.models import Event
from api.serializers import EventSerializer


class EventsViewSet(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(event_type=Event.PUBLIC).all()

