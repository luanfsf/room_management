from django.db import models

DEFAULT_MAX_LENGTH = 100


# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return "Business: " + self.name


class Customer(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return "Customer: " + self.name


class Room(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, default="")
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return "Room: " + self.name


class Event(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, default="")
    business = models.ForeignKey(Business, on_delete=models.PROTECT, null=True)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    date = models.DateField()

    PRIVATE = "private"
    PUBLIC = "public"
    EVENT_TYPE_OPTIONS = [(PRIVATE, "private"), (PUBLIC, "public")]

    event_type = models.CharField(
        max_length=DEFAULT_MAX_LENGTH, choices=EVENT_TYPE_OPTIONS
    )

    def __str__(self):
        return f"Event: {self.name} on {self.date}"

    class Meta:
        unique_together = ("room", "date")


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    booked = models.BooleanField()

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
        *args,
        **kwargs,
    ):
        max_capacity = self.event.room.capacity
        bookings = Booking.objects.filter(event=self.event).count()

        if bookings >= max_capacity:
            raise Exception("Maximum capacity reached.")
        else:
            super(Booking, self).save(*args, **kwargs)

    class Meta:
        unique_together = ("customer", "event")

    def __str__(self):
        return f"Booking: {self.event.name}, {self.event.room.name}, {self.event.date}, {self.customer.name}"
