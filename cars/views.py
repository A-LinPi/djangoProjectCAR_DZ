from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cars


# Create your views here.
def index(request):
    cars = Cars.objects.all()
    return render(request, "index.html", {"cars": cars})


def create(request):
    if request.method == "POST":
        new_car = Cars()
        new_car.mark = request.POST.get("mark")
        new_car.manufacturer = request.POST.get("manufacturer")
        new_car.year = request.POST.get("year")
        new_car.gos_number = request.POST.get("gos_number")
        new_car.save()
    return HttpResponseRedirect("/")

