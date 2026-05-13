from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page_view(request: HttpRequest):
    return render(request, 'main/home_page.html')


def about_us_view(request: HttpRequest):
    return render(request, 'main/about-us.html')


def contact_us_view(request: HttpRequest):
    return render(request, 'main/contact-us.html')


def how_it_works_view(request: HttpRequest):
    return render(request, 'main/how-it-works.html')


def privacy_policy_view(request: HttpRequest):
    return render(request, 'main/privacy-policy.html')


def terms_of_service_view(request: HttpRequest):
    return render(request, 'main/terms-of-service.html')


def cookie_policy_view(request: HttpRequest):
    return render(request, 'main/cookie-policy.html')