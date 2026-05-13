from django.shortcuts import render

# Create your views here.
def profile_view(request):
    return render(request, 'children/profile.html')

def edit_profile_view(request):
    return render(request, 'children/edit-profile.html')

def add_child_view(request):
    return render(request, 'children/add-child.html')