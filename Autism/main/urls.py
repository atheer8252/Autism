from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
<<<<<<< HEAD
    path('', views.home_page_view, name="home"),
=======
    path('home/', views.home_page_view, name="home_page_view"),
>>>>>>> a1db6be34a43dcda900883160d1bd8ced21aa412
    path("about-us/", views.about_us_view, name="about_us"),
    path("contact-us/", views.contact_us_view, name="contact_us"),
    path("how-it-works/", views.how_it_works_view, name="how_it_works"),
    path("privacy-policy/", views.privacy_policy_view, name="privacy_policy"),
    path("terms-of-service/", views.terms_of_service_view, name="terms_of_service"),
    path("cookie-policy/", views.cookie_policy_view, name="cookie_policy"),
]