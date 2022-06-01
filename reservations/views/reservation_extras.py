from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import ReservationExtras
from reservations.forms import ReservationExtrasForm
from reservations.forms import ReservationExtrasSelectForm


# TODO zastanowić się jak ma być wyświetlany ten endpoint (najlepiej gdyby jedna rezerwacja i dodatki do niej)
class ReservationExtrasView(View):
    def get(self, request):
        reservation_extras = [[extra.reservation_id, extra.extras_id] for extra in ReservationExtras.objects.all()]
        return render(request, 'reservation_extras.html', context={'reservation_extras': reservation_extras})


class ReservationExtrasCreateView(FormView):
    pass


class ReservationExtrasUpdateView(UpdateView):
    pass


class ReservationExtrasSelectUpdateView(FormView):
    pass


class ReservationExtrasDeleteView(DeleteView):
    pass


class ReservationExtrasSelectDeleteView(FormView):
    pass







