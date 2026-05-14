from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def activity_list(request:HttpRequest):
        return render(request, 'activity/activity_list.html')

def activity_detail(request:HttpRequest):
        return render(request, 'activity/activity_detail.html')

def activity_result(request:HttpRequest):
        return render(request, 'activity/activity_result.html')

def activity_play(request:HttpRequest):
        return render(request, 'activity/activity_play.html')

def activity_eye(request:HttpRequest):
        return render(request, 'activity/visual_tracking_activity.html')