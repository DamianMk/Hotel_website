from django.contrib import admin
from reservations.models import Extras
from reservations.models import Reservation
from reservations.models import ReservationExtras
from reservations.models import HotelGuest
from reservations.models import Room
from reservations.models import RoomStandard
from reservations.models import RoomFacility
from reservations.models import StandardFacilities
from reservations.models import Employee
from reservations.models import EmployeePosition


# Register your models here.

admin.site.register(Extras)
admin.site.register(Reservation)
admin.site.register(ReservationExtras)
admin.site.register(HotelGuest)
admin.site.register(Room)
admin.site.register(RoomStandard)
admin.site.register(RoomFacility)
admin.site.register(StandardFacilities)
admin.site.register(Employee)
admin.site.register(EmployeePosition)

