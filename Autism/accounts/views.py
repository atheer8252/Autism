from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm

def signup_view(request):
    form = SignUpForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            email = form.cleaned_data['email']

            if User.objects.filter(username=email).exists():
                messages.error(request, 'البريد مستخدم مسبقًا')
                return render(request, 'accounts/signup.html', {'form': form})

            user = User.objects.create_user(
                username=email,
                email=email,
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )

            messages.success(request, 'تم إنشاء الحساب بنجاح')
            return redirect('accounts:signin')

    return render(request, 'accounts/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not email or not password:
            messages.error(request, 'يرجى تعبئة جميع الحقول')
            return render(request, 'accounts/signin.html')

        user = authenticate(
            request,
            username=email,   
            password=password
        )

        if user is not None:
            print(user)
            login(request, user)

            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
                return redirect('main:home_page_view')        
        else:
            messages.error(request, 'بيانات الدخول خاطئة')

    return render(request, 'accounts/signin.html')

def reset_view(request):
    return render(request, 'accounts/reset-password.html')

def guest_login(request):
    request.session['is_guest'] = True
    return redirect('main:home_page_view')
def profile_view(request):
    return render(request, 'accounts/profile.html')

def edit_profile_view(request):
    return render(request, 'accounts/edit-profile.html')
