from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company_list', views.company_list,name='company_list' ),
    path('create_project', views.create_project, name='create_project')
]
