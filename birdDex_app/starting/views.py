from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'starting/index.html')
# Create your views here.

def birdDex(request):
    return render(request, 'starting/birdDex.html')

def camera(request):
    return render(request, 'starting/camera.html')
