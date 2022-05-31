from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import HotelGuest
from reservations.forms import HotelGuestForm
from reservations.forms import HotelGuestSelectForm


class HotelGuestView(View):
    def get(self, request):
        guests = [[guest.name, guest.surname, guest.email_address] for guest in HotelGuest.objects.all()]
        return render(request, 'hotel_guest.html', context={'guests': guests})


class HotelGuestCreateView(FormView):
    template_name = 'form.html'
    form_class = HotelGuestForm
    success_url = reverse_lazy('guests')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        HotelGuest.objects.create(
            name=my_data['name'],
            surname=my_data['surname'],
            email_address=['email_address']
        )
        return result


class HotelGuestUpdateView(UpdateView):
    template_name = 'form.html'
    model = HotelGuest
    form_class = HotelGuestForm
    success_url = reverse_lazy('guests')


class HotelGuestSelectUpdateView(FormView):
    template_name = 'form.html'
    form_class = HotelGuestSelectForm

    def form_valid(self, form):
        return redirect('guest_update', pk=form.cleaned_data['hotel_guest'].id)


class HotelGuestDeleteView(DeleteView):
    template_name = 'hotel_guest_delete.html'
    model = HotelGuest
    success_url = reverse_lazy('guests')


class HotelGuestSelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = HotelGuestSelectForm

    def form_valid(self, form):
        return redirect('guest_delete', pk=form.cleaned_data['hotel_guest'].id)



