from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def all_educational_videos_view (request:HttpResponse):

    return render (request, 'educational_videos/all_videos.html')
