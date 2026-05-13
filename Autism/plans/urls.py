from django.urls import path
from . import views

app_name="plans"

urlpatterns=[
    path('support_plan/', views.support_plan_view, name='support_plan_view')
]