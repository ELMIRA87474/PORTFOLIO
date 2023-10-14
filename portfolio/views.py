from django.shortcuts import render
from .models import Project

def home(reqest):
    projects=Project.objects.all()
    return render(reqest,'portfolio/home.html',{'projects':projects})