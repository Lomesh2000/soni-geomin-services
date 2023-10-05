from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('email', views.email, name='email'),
    path('send_hello_email', views.send_hello_email, name='send_hello_email'),
    path('send_your_own_msg', views.send_your_own_msg, name='send_your_own_msg'),
    path('send_email', views.send_email, name='test server email')
]

