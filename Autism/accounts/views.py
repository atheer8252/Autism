from django.shortcuts import render


def signup_view(request):
    return render(request, 'accounts/signup.html')


def signin_view(request):
    return render(request, 'accounts/signin.html')

def reset_view(request):
    return render(request, 'accounts/reset-password.html')


def profile_view(request):
    return render(request, 'accounts/profile.html')

def edit_profile_view(request):
    return render(request, 'accounts/edit-profile.html')
