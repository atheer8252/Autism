from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import AutismSupportPlace

# Create your views here.

def support_map_view (request:HttpRequest):
    places = AutismSupportPlace.objects.all()

    return render(request,'support_map/support-map.html',{'places': places})

def create_place_view (request:HttpRequest):
    if request.method == "POST":

        AutismSupportPlace.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            region=request.POST.get("region"),
            address=request.POST.get("address"),
            phone_number=request.POST.get("phone_number"),
            website=request.POST.get("website"),
            place_type=request.POST.get("place_type"),
            x_position=request.POST.get("x_position"),
            y_position=request.POST.get("y_position"),
        )

        return redirect("map:support_map_view")

    return render(request,'support_map/create_place.html', {"regions": AutismSupportPlace.REGIONS,"place_types": AutismSupportPlace.PLACE_TYPES})

    





    