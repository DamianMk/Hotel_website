from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View


class HomePage(View):
    def get(self, request):
        return render(request, 'guest_views/index.html')


class HotelDescription(View):
    def get(self, request):
        return render(request, 'guest_views/hotel_description.html')




