from django.shortcuts import render
from main.models import Employee

def employee(request):
    code_objects = Employee.objects.all()  # Обратите внимание на добавленные круглые скобки
    return render(request, 'employee/employee.html', {'code_objects': code_objects})
