from django.shortcuts import render
from .models import Destination, Projects

# Create your views here.

# def index(request):
    
#     dests = Destination.objects.all()

#     return render(request, 'index.html', {'dests':dests})

def index(request):

    projects = Projects.objects.all()
    return render(request, 'index.html', {'projects':projects})

