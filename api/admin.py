from django.contrib import admin

from api.models import Event, Room, Booking, Business, Customer


# Register your models here.
class CustomModelAdminMixin(object):
    """
    Thanks to: https://stackoverflow.com/a/28255245
    """

    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields if field.name != "id"
        ]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


class BusinessAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


class CustomerAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


class RoomAdmin(admin.ModelAdmin):
    pass


class EventAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


class BookingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Business, BusinessAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
