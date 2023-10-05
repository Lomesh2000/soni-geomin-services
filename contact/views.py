from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
from django.core.mail import send_mail
from .forms import EmailForm
from django.conf import settings

def contact(request):
    return render(request, 'contact.html')

def email(request):
    pass

def send_hello_email(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']

        subject = 'New Subscription'
        message = f'Name: {name}\nEmail: {email}'
        from_email = settings.EMAIL_HOST_USER    # Change this to your email
        recipient_list = ['lomeshsoni1234@gmail.com']  # Change this to your email

        send_mail(subject, message, from_email, recipient_list)
        messages.success(request, 'Email sent successfully')

    return render(request, 'send_hello_email.html')

def send_your_own_msg(request):
    if request.method=="POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
            return render(request, 'send_your_own_msg.html')
    else:
        form = EmailForm()
    return render(request, 'send_your_own_msg.html', {'form':form})        

def send_email(request):
    subject = " This Email is from django server"
    message = "This is a test email from django server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['lomeshsoni70@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return redirect('/')