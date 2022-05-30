from django import forms
from reservations.models import Extras
from reservations.models import Reservation
from reservations.models import ReservationExtras
from reservations.models import HotelGuest
from reservations.models import Room
from reservations.models import RoomStandard
from reservations.models import RoomFacility
from reservations.models import Employee
from reservations.models import EmployeePosition


class RoomFacilityForm(forms.ModelForm):
    class Meta:
        model = RoomFacility
        fields = '__all__'

    facility_name = forms.CharField(max_length=50)


class RoomFacilitySelectForm(forms.Form):
    room_facility = forms.ModelChoiceField(queryset=RoomFacility.objects)


class RoomStandardForm(forms.ModelForm):
    class Meta:
        model = RoomStandard
        fields = '__all__'

    standard_name = forms.CharField(max_length=50)
    price = forms.IntegerField()


class RoomStandardSelectForm(forms.Form):
    room_standard = forms.ModelChoiceField(queryset=RoomStandard.objects)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    room_number = forms.IntegerField()
    room_area = forms.IntegerField()
    room_standard_id = forms.ModelChoiceField(queryset=RoomStandard.objects, required=True)


class ExtrasForm(forms.ModelForm):
    class Meta:
        model = Extras
        fields = '__all__'

    name = forms.CharField(max_length=50)
    price = forms.IntegerField()


