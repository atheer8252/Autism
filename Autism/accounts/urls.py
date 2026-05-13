from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup_view,name='signup'),
    path('accounts/signin/', views.signin_view,name='signin'),
    path('accounts/reset/password/', views.reset_view,name='reset'),
    path('accounts/profile/', views.profile_view,name='profile'),
    path('accounts/edit/profile/', views.edit_profile_view,name='edit_profile'),
]
