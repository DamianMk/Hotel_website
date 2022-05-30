from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import RoomFacility
from reservations.forms import RoomFacilityForm
from reservations.forms import RoomFacilitySelectForm


class RoomFacilityView(View):
    def get(self, request):
        facilities = [facility.facility_name for facility in RoomFacility.objects.all()]

        return render(request, 'facility.html', context={'facilities': facilities})


class RoomFacilityCreateView(FormView):
    template_name = 'form.html'
    form_class = RoomFacilityForm
    success_url = reverse_lazy('facilities')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        RoomFacility.objects.create(
            facility_name=my_data['facility_name']
        )
        return result


class RoomFacilityUpdateView(UpdateView):
    template_name = 'form.html'
    model = RoomFacility
    form_class = RoomFacilityForm
    success_url = reverse_lazy('facilities')


class RoomFacilitySelectUpdateView(FormView):
    template_name = 'form.html'
    form_class = RoomFacilitySelectForm

    def form_valid(self, form):
        return redirect('facility_update', pk=form.cleaned_data['room_facility'].id)


class RoomFacilityDeleteView(DeleteView):
    template_name = 'room_facility_delete.html'
    model = RoomFacility
    success_url = reverse_lazy('facilities')


class RoomFacilitySelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = RoomFacilitySelectForm

    def form_valid(self, form):
        return redirect('facility_delete', form.cleaned_data['room_facility'].id)

