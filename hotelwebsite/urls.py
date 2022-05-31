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
from reservations.views.room import RoomUpdateView
from reservations.views.room import RoomSelectUpdateView
from reservations.views.room import RoomDeleteView
from reservations.views.room import RoomSelectDeleteView
from reservations.views.room_standard import RoomStandardView
from reservations.views.room_standard import RoomStandardCreateView
from reservations.views.room_standard import RoomStandardUpdateView
from reservations.views.room_standard import RoomStandardSelectUpdateView
from reservations.views.room_standard import RoomStandardDeleteView
from reservations.views.room_standard import RoomStandardSelectDeleteView
from reservations.views.facility import FacilityView
from reservations.views.facility import FacilityCreateView
from reservations.views.facility import FacilityUpdateView
from reservations.views.facility import FacilitySelectUpdateView
from reservations.views.facility import FacilityDeleteView
from reservations.views.facility import FacilitySelectDeleteView
from reservations.views.extras import ExtrasView
from reservations.views.extras import ExtrasCreateView
from reservations.views.extras import ExtrasUpdateView
from reservations.views.extras import ExtrasSelectUpdate
from reservations.views.extras import ExtrasDeleteView
from reservations.views.extras import ExtrasSelectDeleteView
from reservations.views.hotel_guest import HotelGuestView
from reservations.views.hotel_guest import HotelGuestCreateView
from reservations.views.hotel_guest import HotelGuestUpdateView
from reservations.views.hotel_guest import HotelGuestSelectUpdateView
from reservations.views.hotel_guest import HotelGuestDeleteView
from reservations.views.hotel_guest import HotelGuestSelectDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms', RoomView.as_view(), name='rooms'),
    path('room/create', RoomCreateView.as_view()),
    path('room/update/<pk>', RoomUpdateView.as_view(), name='room_update'),
    path('room/update', RoomSelectUpdateView.as_view()),
    path('room/delete/<pk>', RoomDeleteView.as_view(), name='room_delete'),
    path('room/delete', RoomSelectDeleteView.as_view()),
    path('standards', RoomStandardView.as_view(), name='room_standards'),
    path('standard/create', RoomStandardCreateView.as_view()),
    path('standard/update/<pk>', RoomStandardUpdateView.as_view(), name='standard_update'),
    path('standard/update', RoomStandardSelectUpdateView.as_view()),
    path('standard/delete/<pk>', RoomStandardDeleteView.as_view(), name='standard_delete'),
    path('standard/delete', RoomStandardSelectDeleteView.as_view()),
    path('facilities', FacilityView.as_view(), name='facilities'),
    path('facility/create', FacilityCreateView.as_view()),
    path('facility/update/<pk>', FacilityUpdateView.as_view(), name='facility_update'),
    path('facility/update', FacilitySelectUpdateView.as_view()),
    path('facility/delete/<pk>', FacilityDeleteView.as_view(), name='facility_delete'),
    path('facility/delete', FacilitySelectDeleteView.as_view()),
    path('extras', ExtrasView.as_view(), name='extras'),
    path('extras/create', ExtrasCreateView.as_view()),
    path('extras/update/<pk>', ExtrasUpdateView.as_view(), name='extras_update'),
    path('extras/update', ExtrasSelectUpdate.as_view()),
    path('extras/delete/<pk>', ExtrasDeleteView.as_view(), name='extras_delete'),
    path('extras/delete', ExtrasSelectDeleteView.as_view()),
    path('guests', HotelGuestView.as_view(), name='guests'),
    path('guest/create', HotelGuestCreateView.as_view()),
    path('guest/update/<pk>', HotelGuestUpdateView.as_view(), name='guest_update'),
    path('guest/update', HotelGuestSelectUpdateView.as_view()),
    path('guest/delete/<pk>', HotelGuestDeleteView.as_view(), name='guest_delete'),
    path('guest/delete', HotelGuestSelectDeleteView.as_view()),

]
