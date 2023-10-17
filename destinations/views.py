from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from travello.models import Destination
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

# def destination(request, city_name):
#     city = get_object_or_404(Destination, name=city_name)
#     return render(request, 'destinations.html', {'name':city.name})