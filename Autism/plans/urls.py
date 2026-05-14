from django.urls import path
from . import views

app_name="plans"

urlpatterns=[
    path('main_plan/', views.main_plan_view, name='main_plan_view'),
    path('support_plan/', views.support_plan_view, name='support_plan_view')
]