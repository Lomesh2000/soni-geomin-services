from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from travello.models import Destination, Projects
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required

def mumbai(request):

    if not request.user.is_authenticated :
        return redirect('login')
    else:

        return render(request, 'destinations.html', {'name':'mumbai'})

@login_required(login_url='login')
def delhi(request):
    return render(request, 'destinations.html', {'name':'delhi'})


@login_required(login_url='login')
def bangalore(request):
    return render(request, 'destinations.html', {'name':'bangalore'})


@login_required(login_url='login')
def ultratech(request):
    return render(request, 'destinations.html', {'name':'ultratech'})


## dynamically creating urls for the data pressent
@login_required(login_url="login")
def dynamic_url(request,id):
    
    item = get_object_or_404(Projects, id = id)
    return render(request, 'destinations.html', {'item':item})

