from django.urls import path
from . import views

app_name="map"

urlpatterns=[
    path('support/map/' , views.support_map_view,  name='support_map_view'),
    path('create/place', views.create_place_view, name='create_place_view')
]