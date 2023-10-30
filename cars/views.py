from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
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


def edit(request, id):
    try:
        car = Cars.objects.get(id=id)

        if request.method == "POST":
            car.mark = request.POST.get("mark")
            car.manufacturer = request.POST.get("manufacturer")
            car.year = request.POST.get("year")
            car.gos_number = request.POST.get("gos_number")
            car.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_car.html", {"car": car})
    except Cars.DoesNotExist:
        return HttpResponseNotFound("<h2>Автомобиль не найден</h2>")


def delete(request, id):
    try:
        car = Cars.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect("/")
    except Cars.DoesNotExist:
        return HttpResponseNotFound("<h2>Автомобиль не найден</h2>")
