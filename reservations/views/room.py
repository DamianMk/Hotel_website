from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from reservations.models import Room
from reservations.forms import RoomForm


class RoomView(View):
    def get(self, request):
        rooms = []
        for room in Room.objects.all():
            data = [room.room_number, room.room_area, room.room_standard_id]
            rooms.append(data)

        return render(request, 'room.html', context={'rooms': rooms})


class RoomCreateView(FormView):
    template_name = 'form.html'
    form_class = RoomForm
    success_url = reverse_lazy('rooms')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        Room.objects.create(
            room_number=my_data['room_number'],
            room_area=my_data['room_area'],
            room_standard_id=my_data['room_standard_id']
        )
        return result





