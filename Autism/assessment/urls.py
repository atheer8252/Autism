from django.urls import path
from . import views

app_name="assessment"

urlpatterns=[
    path('upload/', views.upload_video, name="upload_video"),
]