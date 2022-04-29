from django.shortcuts import render, redirect
from .forms import carlistForm
from .models import carlist, Show_room

def Home(request):
    all_cars=carlist.objects.all()
    return render(request,"index.html",{"cars":all_cars})

def add(request):
    if request.method=='POST':
        print(request.POST)
        form=carlistForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/Home/')
    else:
        form=carlistForm()
    return render(request, 'Add New Car.html', {'form':form})

def Search(request, CarName):
    option=carlist.objects.filter(CarName__icontains=CarName)
    return render(request,"search.html",{"carrecord":option})

def Showroom(request, Name):
    A=Show_room.objects.filter(Name__icontains=Name)
    return render(request,"showroom.html",{"record":A})

def edit(request, CarName):
    car_data=carlist.objects.get(Name=CarName)
    form=carlistForm(instance=car_data)
    return render(request, 'update.html',{'form':form, 'Name':CarName})

def update(request, CarName):
    car_data=carlist.objects.get(Name=CarName)
    form=carlistForm(request.POST, instance=car_data)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request, 'update.html', {'form':form, 'Name':CarName})