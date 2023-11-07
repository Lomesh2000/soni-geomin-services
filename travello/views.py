from django.shortcuts import render
from rest_framework.response import Response
from .models import Destination, Projects
from travello.serializer import ProjectsSerializers
from rest_framework.decorators import api_view

# Create your views here.

# def index(request):
    
#     dests = Destination.objects.all()

#     return render(request, 'index.html', {'dests':dests})

def index(request):

    projects = Projects.objects.all()
    return render(request, 'index.html', {'projects':projects})

@api_view(['GET'])
def company_list(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializers(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_project(request):
    # if request.method=='POST':
        
    serializer = ProjectsSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print('Valid')
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


    # elif request.method == 'GET':

    #     projects = Projects.objects.all()
    #     serializer = ProjectsSerializers(projects, many=True)
    #     return Response(serializer.data)