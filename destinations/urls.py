from django.urls import path

from . import views

urlpatterns = [
    path('mumbai', views.mumbai, name='mumbai'),
    path('delhi', views.delhi, name='delhi'),
    path('bangalore', views.bangalore, name='banaglore'),
    path('ultratech',views.ultratech, name='ultratech'),
    path('<int:id>', views.dynamic_url, name='all')
]
