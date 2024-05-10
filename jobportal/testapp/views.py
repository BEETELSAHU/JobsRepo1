from django.shortcuts import render
from testapp.models import *

# Create your views here.
def home_view(request):
    return render(request, 'htmlfiles/home.html')

def hydjob_view(request):
    job_list = HydJobs.objects.all()
    name = 'Hyderabad'
    my_dict = {'name':name, 'jobs':job_list}
    return render(request, 'htmlfiles/content.html', my_dict)

def bngjob_view(request):
    job_list = BngJobs.objects.all()
    name = 'Bangalore'
    my_dict = {'name':name,'jobs':job_list}
    return render(request, 'htmlfiles/content.html', my_dict)

def punejob_view(request):
    job_list = PuneJobs.objects.all()
    name = 'Pune'
    my_dict = {'name':name,'jobs':job_list}
    return render(request, 'htmlfiles/content.html', my_dict)