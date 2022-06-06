from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.


class Facility(models.Model):
    facility_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.facility_name}'


class RoomStandard(models.Model):
    standard_name = models.CharField(max_length=50)
    price = models.SmallIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.standard_name}'


class Room(models.Model):
    room_number = models.SmallIntegerField(validators=[MinValueValidator(0)])
    room_area = models.SmallIntegerField(validators=[MinValueValidator(0)])
    room_standard_id = models.ForeignKey(RoomStandard, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Pokój numer {self.room_number}'


class RoomFacility(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    room_facility_id = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True)


class Extras(models.Model):
    name = models.CharField(max_length=50)
    price = models.SmallIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.name}'


class HotelGuest(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)

    def __str__(self):
        return f'{self.name} {self.surname} | {self.email_address}'


class Reservation(models.Model):
    reservation_number = models.CharField(max_length=50)
    booking_date = models.DateField(auto_now_add=True, editable=False)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.SmallIntegerField()
    hotel_guest_id = models.ForeignKey(HotelGuest, on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Rezerwacja numer {self.reservation_number}'


class ReservationExtras(models.Model):
    reservation_id = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    extras_id = models.ForeignKey(Extras, on_delete=models.SET_NULL, null=True)


class EmployeePosition(models.Model):
    position_name = models.CharField(max_length=50)
    permission_level = models.SmallIntegerField()

    def __str__(self):
        return f'{self.position_name}'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    employee_position_id = models.ForeignKey(EmployeePosition, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
