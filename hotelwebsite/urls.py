"""hotelwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from reservations.views.room import RoomView
from reservations.views.room import RoomCreateView
from reservations.views.room_standard import RoomStandardView
from reservations.views.room_standard import RoomStandardCreateView
from reservations.views.room_standard import RoomStandardUpdateView
from reservations.views.room_standard import RoomStandardSelectUpdateView
from reservations.views.room_standard import RoomStandardDeleteView
from reservations.views.room_standard import RoomStandardSelectDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms', RoomView.as_view(), name='rooms'),
    path('room/create', RoomCreateView.as_view()),
    path('standards', RoomStandardView.as_view(), name='room_standards'),
    path('standard/create', RoomStandardCreateView.as_view()),
    path('standard/update/<pk>', RoomStandardUpdateView.as_view(), name='standard_update'),
    path('standard/update', RoomStandardSelectUpdateView.as_view()),
    path('standard/delete/<pk>', RoomStandardDeleteView.as_view(), name='standard_delete'),
    path('standard/delete', RoomStandardSelectDeleteView.as_view()),
]
