from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import RoomStandard
from reservations.models import Room
from reservations.forms import RoomStandardForm
from reservations.forms import RoomStandardSelectForm


class RoomStandardView(View):
    def get(self, request):
        standards = []
        for standard in RoomStandard.objects.all():
            data = [standard.standard_name, standard.price]
            standards.append(data)

        return render(request, 'room_standard.html', context={'standards': standards})


class RoomStandardGuestView(View):
    def get(self, request):
        standards = RoomStandard.objects.all()
        rooms = Room.objects.all()
        room_sizes = {}
        for standard in standards:
            areas = []
            for room in rooms:
                if room.room_standard_id == standard:
                    areas.append(room.room_area)
            room_sizes[standard.standard_name] = [min(areas), max(areas)]

        return render(request, 'guest_views/standards.html', context={'standards': standards,
                                                                      'room_sizes': room_sizes})


class RoomStandardCreateView(FormView):
    template_name = 'form.html'
    form_class = RoomStandardForm
    success_url = reverse_lazy('room_standards')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        print(my_data)
        RoomStandard.objects.create(
            standard_name=my_data['standard_name'],
            price=my_data['price']
        )
        return result


class RoomStandardUpdateView(UpdateView):
    template_name = 'form.html'
    model = RoomStandard
    form_class = RoomStandardForm
    success_url = reverse_lazy('room_standards')


class RoomStandardSelectUpdateView(FormView):
    template_name = 'form.html'
    form_class = RoomStandardSelectForm

    def form_valid(self, form):
        return redirect('standard_update', pk=form.cleaned_data['room_standard'].id)


class RoomStandardDeleteView(DeleteView):
    template_name = 'room_standard_delete.html'
    model = RoomStandard
    success_url = reverse_lazy('room_standards')


class RoomStandardSelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = RoomStandardSelectForm

    def form_valid(self, form):
        return redirect('standard_delete', pk=form.cleaned_data['room_standard'].id)

