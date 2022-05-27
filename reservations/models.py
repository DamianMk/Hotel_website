from django.db import models

# Create your models here.


class RoomFacility(models.Model):
    facility_name = models.CharField(max_length=50)


class RoomStandard(models.Model):
    standard_name = models.CharField(max_length=50)
    price = models.SmallIntegerField()
    room_facility_id = models.ForeignKey(RoomFacility, on_delete=models.SET_NULL, null=True)


class Room(models.Model):
    room_number = models.SmallIntegerField()
    room_area = models.SmallIntegerField()
    room_standard_id = models.ForeignKey(RoomStandard, on_delete=models.SET_NULL, null=True)


class Extras(models.Model):
    name = models.CharField(max_length=50)
    price = models.SmallIntegerField()


class HotelGuest(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)


class Reservation(models.Model):
    reservation_number = models.CharField(max_length=50)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.SmallIntegerField()
    hotel_guest_id = models.ForeignKey(HotelGuest, on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)


class ReservationExtras(models.Model):
    reservation_id = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    extras_id = models.ForeignKey(Extras, on_delete=models.SET_NULL, null=True)


class EmployeePosition(models.Model):
    position_name = models.CharField(max_length=50)
    permission_level = models.SmallIntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    employee_position_id = models.ForeignKey(EmployeePosition, on_delete=models.SET_NULL, null=True)



