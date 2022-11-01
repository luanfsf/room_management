from django.urls import path, include
from rest_framework import routers

from api import views

"""room_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()

business_urls = [
    path("business/", views.BusinessViewSet.as_view(), name="business_list"),
    path("business/<int:pk>/", views.BusinessViewSet.as_view(), name="business"),
]
customer_urls = [
    path("customer/", views.CustomerViewSet.as_view(), name="customers_list"),
    path("customer/<int:pk>/", views.CustomerViewSet.as_view(), name="customer"),
]

room_urls = [
    path("room/", views.RoomViewSet.as_view(), name="rooms_list"),
    path("room/<int:pk>/", views.RoomViewSet.as_view(), name="room"),
]

event_urls = [
    path("event/", views.EventsViewSet.as_view(), name="events_list"),
    path("event/<int:pk>/", views.EventsViewSet.as_view(), name="event"),
]

booking_urls = [
    path("booking/", views.BookingViewSet.as_view(), name="bookings_list"),
    path("booking/<int:pk>/", views.BookingViewSet.as_view(), name="booking"),
]

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include(router.urls)),
    ]
    + business_urls
    + customer_urls
    + room_urls
    + event_urls
    + booking_urls
)
