from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import Room
from reservations.forms import RoomForm
from reservations.forms import RoomSelectForm


class RoomView(View):
    def get(self, request):
        rooms = []
        for room in Room.objects.all():
            data = [room.room_number, room.room_area, room.room_standard_id]
            rooms.append(data)

        return render(request, 'rooms.html', context={'rooms': rooms})


class SingleRoomView(View):
    def get(self, request):
        room = [Room.room_number, Room.room_standard_id, Room.room_area]
        return render(request, 'room.html', context={'room': room})


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


class RoomUpdateView(UpdateView):
    template_name = 'form.html'
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('rooms')


class RoomSelectUpdateView(FormView):
    template_name = 'form.html'
    form_class = RoomSelectForm

    def form_valid(self, form):
        return redirect('room_update', pk=form.cleaned_data['room'].id)


class RoomDeleteView(DeleteView):
    template_name = 'room_delete.html'
    model = Room
    success_url = reverse_lazy('rooms')


class RoomSelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = RoomSelectForm

    def form_valid(self, form):
        return redirect('room_delete', pk=form.cleaned_data['room'].id)

