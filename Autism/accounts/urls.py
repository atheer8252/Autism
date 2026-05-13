from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view,name='signup'),
    path('signin/', views.signin_view,name='signin'),
    path('reset/password/', views.reset_view,name='reset'),
    path('profile/', views.profile_view,name='profile'),
    path('edit/profile/', views.edit_profile_view,name='edit_profile'),


]
