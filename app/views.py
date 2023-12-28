from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EmployeeDetail

# Create your views here.
def home(request):
    all_employee = EmployeeDetail.objects.all()
    context = {
        'all_employee' : all_employee
    }
    return render (request, 'home.html', context)

def employee_detail(request, pk):
    try:
        employee = EmployeeDetail.objects.get(pk=pk)
        context = {
            'employee' : employee
        }
        return render(request, 'employee_details.html', context)
    except:
        return redirect('home')