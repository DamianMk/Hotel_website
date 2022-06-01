from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from reservations.models import Employee
from reservations.forms import EmployeeForm
from reservations.forms import EmployeeSelectForm


class EmployeeView(View):
    def get(self, request):
        employees = [[e.name, e.surname, e.employee_position_id] for e in Employee.objects.all()]
        return render(request, 'employee.html', context={'employees': employees})


class EmployeeCreateView(FormView):
    template_name = 'form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        result = super().form_valid(form)
        my_data = form.cleaned_data
        Employee.objects.create(
            name=my_data['name'],
            surname=my_data['surname'],
            employee_position_id=my_data['employee_position_id']
        )
        return result


class EmployeeUpdateView(UpdateView):
    template_name = 'form.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')


class EmployeeSelectUpdateView(FormView):
    template_name = 'form.html'
    form_class = EmployeeSelectForm

    def form_valid(self, form):
        return redirect('employee_update', pk=form.cleaned_data['employee'].id)


class EmployeeDeleteView(DeleteView):
    template_name = 'employee_delete.html'
    model = Employee
    success_url = reverse_lazy('employees')


class EmployeeSelectDeleteView(FormView):
    template_name = 'form.html'
    form_class = EmployeeSelectForm

    def form_valid(self, form):
        return redirect('employee_delete', pk=form.cleaned_data['employee'].id)

