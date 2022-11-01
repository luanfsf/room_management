from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'room', 'date', 'event_type']
