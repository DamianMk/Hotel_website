from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import Extras
from reservations.forms import ExtrasForm
from reservations.forms import ExtrasSelectForm


class ExtrasView(View):
    def get(self, request):
        extras = [[extras.name, extras.price] for extras in Extras.objects.all()]
        return render(request, 'extras.html', context={'extras': extras})


class ExtrasCreateView(FormView):
    template_name = 'form.html'
    form_class = ExtrasForm
    success_url = reverse_lazy('extras')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        Extras.objects.create(
            name=my_data['name'],
            price=my_data['price']
        )
        return result


class ExtrasUpdateView(UpdateView):
    template_name = 'form.html'
    model = Extras
    form_class = ExtrasForm
    success_url = reverse_lazy('extras')


class ExtrasSelectUpdate(FormView):
    template_name = 'form.html'
    form_class = ExtrasSelectForm

    def form_valid(self, form):
        return redirect('extras_update', pk=form.cleaned_data['extras'].id)


class ExtrasDeleteView(DeleteView):
    template_name = 'extras_delete.html'
    model = Extras
    success_url = reverse_lazy('extras')


class ExtrasSelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = ExtrasSelectForm

    def form_valid(self, form):
        return redirect('extras_delete', pk=form.cleaned_data['extras'].id)

