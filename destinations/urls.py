from django.urls import path

from . import views

urlpatterns = [
    path('mumbai', views.mumbai, name='mumbai'),
    path('delhi', views.delhi, name='delhi'),
    path('bangalore', views.bangalore, name='banaglore')
    
]
