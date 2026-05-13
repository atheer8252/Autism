from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
     path('home/', views.home_page_view, name="home_page_view"),
    path("about-us/", views.about_us, name="about_us"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-of-service/", views.terms_of_service, name="terms_of_service"),
    path("cookie-policy/", views.cookie_policy, name="cookie_policy"),
]