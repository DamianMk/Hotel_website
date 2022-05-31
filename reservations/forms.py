from django import forms
from reservations.models import Extras
from reservations.models import Reservation
from reservations.models import ReservationExtras
from reservations.models import HotelGuest
from reservations.models import Room
from reservations.models import RoomStandard
from reservations.models import Facility
from reservations.models import StandardFacilities
from reservations.models import Employee
from reservations.models import EmployeePosition


class HotelGuestForm(forms.ModelForm):
    class Meta:
        model = HotelGuest
        fields = '__all__'

    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email_address = forms.EmailField()


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

