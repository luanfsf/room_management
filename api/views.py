# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Event, Business, Customer, Room, Booking
from api.serializers import (
    EventSerializer,
    BusinessSerializer,
    CustomerSerializer,
    RoomSerializer,
    BookingSerializer,
)


class BusinessViewSet(
    generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        return Business.objects.all()


class CustomerViewSet(
    generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()


class RoomViewSet(
    generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.event_set.count():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "There are events for that room."},
            )
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class EventsViewSet(
    generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(event_type=Event.PUBLIC).all()


class BookingViewSet(
    generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.all()

    def create(self, request, *args, **kwargs):
        event_id = request.data.get("event")
        event = Event.objects.get(id=event_id)

        max_capacity = event.room.capacity
        bookings = Booking.objects.filter(event_id=event_id).count()

        if bookings >= max_capacity:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "Maximum capacity reached."},
            )
        if event.event_type == Event.PRIVATE:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "Default users cannot create events for private events."},
            )
        else:
            return super(BookingViewSet, self).create(request, *args, **kwargs)
