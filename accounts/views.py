from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError

from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password2)
        user.save()
        print("user oreated")
        if user is not None:
            return redirect('register')

        else:
            return redirect('/')

    else:
        return render(request, 'register.html')

