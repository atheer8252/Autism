from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/guest/', views.guest_login, name='guest_login'),
    path('', views.signup_view,name='signup'),
    path('accounts/signin/', views.signin_view,name='signin'),
    path('accounts/reset/password/', views.reset_view,name='reset'),
    path('accounts/profile/', views.profile_view,name='profile'),
    path('accounts/edit/profile/', views.edit_profile_view,name='edit_profile'),
    path('accounts/settings', views.settings_view,name='settings'),
    path('accounts/likes', views.likes_view,name='likes'),
]
