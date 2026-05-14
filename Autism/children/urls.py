from django.urls import path
from . import views

app_name = 'children'

urlpatterns = [
    path('profile/', views.profile_view,name='profile'),
    path('edit/profile/', views.edit_profile_view,name='edit_profile'),
    path('add/child/', views.add_child_view,name='add_child'),
]