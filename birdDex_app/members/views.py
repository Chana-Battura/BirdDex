from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#include 18:30 of login with user authentication video tutorial with codemy for messages
# Create your views here.

def login_user(request):
    if (request.method == "POST"):
        #give inputs on login page names of username and password
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else: 
            messages.success(request, "There was an error logging in, try again or register your account.")
        
    else:
        return render(request, 'authentication/login.html', {})
