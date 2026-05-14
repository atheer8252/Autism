from django.urls import path
from . import views

app_name="activity"

urlpatterns=[
    path('activity_list/', views.activity_list, name="activity_list"),
    path('activity_detail/', views.activity_detail, name="activity_detail"),
    path('activity_result/', views.activity_result, name="activity_result"),
    path('activity_play/', views.activity_play, name="activity_play"),
    path('activity_eye/', views.activity_eye, name="activity_eye"),
]