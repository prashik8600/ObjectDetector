from django.db import models
from django.shortcuts import render
from .forms import ImageForm
from .models import img
import xml.etree.ElementTree as ET
from .models import img
import cv2
# import numpy as np 
from django.conf import settings
import os


def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            fname = form.cleaned_data['files'].name
            imgname = form.cleaned_data['photo'].name
            form.save()
            imagePath = 'media/allimg/'+imgname
            cascPath = 'media/documents/'+fname
            tree =ET.parse(cascPath)
            root =tree.getroot()
            d = {}
            lst = []
            for i in root.findall('object'):
                for j in i.findall('bndbox/'):
                    d['name'] = i[0].text
                    d[j.tag] = j.text
                for item in d.items():
                    if item[0]=='name':
                        name=item[1]
                    if item[0]=='xmin':
                        xmin=int(item[1])
                    if item[0]=='xmax':       
                        xmax=int(item[1])
                    if item[0]=='ymin':
                        ymin=int(item[1])
                    if item[0]=='ymax':    
                        ymax=int(item[1])
                        break
            image=cv2.imread('media/allimg/'+imgname)
            original=image.copy()
            gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            thresh=cv2.threshold(gray,0,100,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            cv2.rectangle(image, ((xmin), (ymin)), ((xmax), (ymax)), (0,0,255), 2)
            output='media/finalop/FOP.jpg' 
            cv2.imwrite(output,image)
            # Code is not completed
    form = ImageForm()
    imgs = img.objects.all()
    return render(request, 'myapp/home.html', {'imgs': imgs, 'form': form})

