from django.urls import path
from . import views

app_name="community"

urlpatterns=[
    path('community/' , views.community_view, name='community_view'),
    path('create_post/', views.create_post_view, name='create_post_view'),
    path('details_post/', views.details_post_view, name='details_post_view'),
]