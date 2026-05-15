from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def community_view (request:HttpResponse):

    return render (request, 'community/community_feed.html')

def create_post_view (request:HttpResponse):

    return render (request, 'community/create_post.html')

def details_post_view (request:HttpResponse):

    return render (request, 'community/details_post.html')
