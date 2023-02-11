from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Trip, Gear
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GearForm


def home(request):
    return render(request, 'index.html', context={})


def about(request):
    return render(request, 'about.html')


def gear(request):
    gears = Gear.objects.all()
    return render(request, 'gear/index.html', {'gears': gears})


def gear_detail(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    gear_form = GearForm()
    return render(request, 'gear/detail.html', {'gear': gear, 'gear_form': gear_form})


def trip_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', {'trips': trips})


def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    # gear_trip_doesnt_have = Trip.objects.exclude(
    #     id__in=trip.gear.all().values_list('id'))
    return render(request, 'trips/detail.html', {
        'trip': trip,
        # 'gear': gear_trip_doesnt_have
    })


class TripCreate(CreateView):
    model = Trip
    fields = '__all__'
    success_url = '/trips/'


class TripUpdate(UpdateView):
    model = Trip
    fields = '__all__'


class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'


class GearCreate(CreateView):
    model = Gear
    fields = ['name', 'use', 'size', 'brand', 'model', 'necessary']
    success_url = '/gear/'


class GearUpdate(UpdateView):
    model = Gear
    fields = '__all__'


class GearDelete(DeleteView):
    model = Gear
    success_url = '/gear/'
