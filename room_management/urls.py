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

event_urls = [
    path('events/', views.EventsViewSet.as_view(), name="events_list"),
    path('events/<int:pk>/', views.EventsViewSet.as_view(), name="events"),
]

room_urls = [
    path('rooms/', views.RoomViewSet.as_view(), name="rooms_list"),
    path('rooms/<int:pk>/', views.RoomViewSet.as_view(), name="rooms"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
] + event_urls + room_urls
