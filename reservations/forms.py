import datetime

from django import forms
from reservations.models import Extras
from reservations.models import Reservation
from reservations.models import ReservationExtras
from reservations.models import HotelGuest
from reservations.models import Room
from reservations.models import RoomStandard
from reservations.models import Facility
from reservations.models import RoomFacility
from reservations.models import Employee
from reservations.models import EmployeePosition


class HotelGuestForm(forms.ModelForm):
    class Meta:
        model = HotelGuest
        fields = '__all__'

    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)


class HotelGuestSelectForm(forms.Form):
    hotel_guest = forms.ModelChoiceField(queryset=HotelGuest.objects)


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'

    facility_name = forms.CharField(max_length=50)


class FacilitySelectForm(forms.Form):
    facility = forms.ModelChoiceField(queryset=Facility.objects)


class RoomStandardForm(forms.ModelForm):
    class Meta:
        model = RoomStandard
        fields = '__all__'

    standard_name = forms.CharField(max_length=50)
    price = forms.IntegerField()


class RoomStandardSelectForm(forms.Form):
    room_standard = forms.ModelChoiceField(queryset=RoomStandard.objects)


class StandardFacilitiesForm(forms.Form):
    room_standard_id = forms.ModelChoiceField(queryset=RoomStandard.objects, required=False)
    room_faciltiy_id = forms.ModelChoiceField(queryset=Facility.objects, required=False)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    room_number = forms.IntegerField()
    room_area = forms.IntegerField()
    room_standard_id = forms.ModelChoiceField(queryset=RoomStandard.objects, required=True)


class RoomSelectForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Room.objects)


class ExtrasForm(forms.ModelForm):
    class Meta:
        model = Extras
        fields = '__all__'

    name = forms.CharField(max_length=50)
    price = forms.IntegerField()


class ExtrasSelectForm(forms.Form):
    extras = forms.ModelChoiceField(queryset=Extras.objects)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    reservation_number = forms.CharField(max_length=50)
    check_in_date = forms.DateField(widget=forms.SelectDateWidget())
    check_out_date = forms.DateField(widget=forms.SelectDateWidget())
    number_of_guests = forms.IntegerField()
    hotel_guest_id = forms.ModelChoiceField(queryset=HotelGuest.objects, required=True)
    room_id = forms.ModelChoiceField(queryset=Room.objects, required=True)

    def clean(self):
        data = super(ReservationForm, self).clean()
        check_in = self.cleaned_data['check_in_date']
        check_out = self.cleaned_data['check_out_date']
        if check_in > check_out:
            self.add_error('check_in_date', 'Data przyjazdu nie może być później niż data wyjazdu.')
        elif check_in < datetime.date.today():
            self.add_error('check_in_date', 'Nie można zarezerwować daty wstecz.')
        return data


class ReservationSelectForm(forms.Form):
    reservation = forms.ModelChoiceField(queryset=Reservation.objects)


class ReservationExtrasForm(forms.ModelForm):
    class Meta:
        model = ReservationExtras
        fields = '__all__'

    reservation_id = forms.ModelChoiceField(queryset=Reservation.objects, required=True)
    extras_id = forms.ModelChoiceField(queryset=Extras.objects, required=True)


class ReservationExtrasSelectForm(forms.Form):
    reservation_extras = forms.ModelChoiceField(queryset=ReservationExtras.objects)


class EmployeePositionForm(forms.ModelForm):
    class Meta:
        model = EmployeePosition
        fields = '__all__'

    position_name = forms.CharField(max_length=50)
    permission_level = forms.IntegerField()


class EmployeePositionSelectForm(forms.Form):
    employee_position = forms.ModelChoiceField(queryset=EmployeePosition.objects)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    employee_position_id = forms.ModelChoiceField(queryset=EmployeePosition.objects)


class EmployeeSelectForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects)

