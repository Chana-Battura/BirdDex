from django.http.response import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from . import forms
import base64
from PIL import Image
import numpy as np
import random
from io import BytesIO
from keras.models import load_model
from keras.preprocessing import image
from keras.utils.np_utils import to_categorical
import csv

def index(request):
    return render(request, 'starting/index.html')
# Create your views here.

def birdDex(request):
    return render(request, 'starting/birdDex.html')

def camera(request):
    if request.method == 'POST':
        form = forms.JoinForm(request.POST)

        if form.is_valid():
            image_64 = form.cleaned_data['image']
            dict_from_csv = {}

            with open('MlTest/class_dict.csv', mode='r') as inp:
                reader = csv.reader(inp)
                dict_from_csv = {rows[0]:rows[1] for rows in reader}

            model = load_model("MlTest/BirdModel.h5")
            img=Image.open(BytesIO(base64.b64decode(image_64)))
            img = img.convert('RGB')
            img=img.resize((112,112))
            img=np.expand_dims(img, axis=0)
            pred=model.predict(img)
            index=np.argmax(pred[0])
            klass=dict_from_csv[str(index)]
            probability=pred[0][index]*100
            print(probability)
            return render(request, f"starting/birddex/{klass}.html")

    else:
        form = forms.JoinForm()


    return render(request, 'starting/camera.html', {'form': form})