from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import Facility
from reservations.forms import FacilityForm
from reservations.forms import FacilitySelectForm


class FacilityView(View):
    def get(self, request):
        facilities = [facility.facility_name for facility in Facility.objects.all()]
        return render(request, 'facility.html', context={'facilities': facilities})


class FacilityCreateView(FormView):
    template_name = 'form.html'
    form_class = FacilityForm
    success_url = reverse_lazy('facilities')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        Facility.objects.create(
            facility_name=my_data['facility_name']
        )
        return result


class FacilityUpdateView(UpdateView):
    template_name = 'form.html'
    model = Facility
    form_class = FacilityForm
    success_url = reverse_lazy('facilities')


class FacilitySelectUpdateView(FormView):
    template_name = 'form.html'
    form_class = FacilitySelectForm

    def form_valid(self, form):
        return redirect('facility_update', pk=form.cleaned_data['room_facility'].id)


class FacilityDeleteView(DeleteView):
    template_name = 'facility_delete.html'
    model = Facility
    success_url = reverse_lazy('facilities')


class FacilitySelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = FacilitySelectForm

    def form_valid(self, form):
        return redirect('facility_delete', form.cleaned_data['facility'].id)




