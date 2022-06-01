from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import Reservation
from reservations.forms import ReservationForm
from reservations.forms import ReservationSelectForm


class ReservationsView(View):
    def get(self, request):
        reservations = [reservation for reservation in Reservation.objects.all()]
        return render(request, 'reservations.html', context={'reservations': reservations})


class ReservationCreateView(FormView):
    template_name = 'form.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservations')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        Reservation.objects.create(
            reservation_number=my_data['reservation_number'],
            booking_date=my_data['booking_date'],
            check_in_date=my_data['check_in_date'],
            check_out_date=my_data['check_out_date'],
            number_of_guests=my_data['number_of_guests'],
            hotel_guest_id=my_data['hotel_guest_id'],
            room_id=my_data['room_id']
        )
        return result


class ReservationUpdateView(UpdateView):
    template_name = 'form.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservations')


class ReservationSelectUpdateView(FormView):
    template_name = 'form.html'
    form_class = ReservationSelectForm

    def form_valid(self, form):
        return redirect('reservation_update', pk=form.cleaned_data['reservation'].id)


class ReservationDeleteView(DeleteView):
    template_name = 'reservation_delete.html'
    model = Reservation
    success_url = reverse_lazy('reservations')


class ReservationSelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = ReservationSelectForm

    def form_valid(self, form):
        return redirect('reservation_delete', pk=form.cleaned_data['reservation'].id)



