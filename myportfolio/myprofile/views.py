from django.shortcuts import render
from.models import myprofile

def home(request):
    jobs = myprofile.objects
    return render(request,'myprofile/home.html',{'jobs':jobs})
