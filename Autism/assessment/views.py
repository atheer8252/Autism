from django.shortcuts import render 
from django.http import HttpRequest, HttpResponse


# Create your views here.

def upload_video(request:HttpRequest):
    return render(request, 'assessment/upload_video.html')

def questionnaire(request:HttpRequest):
    return render(request, 'assessment/questionnaire.html')