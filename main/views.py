from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Trip, Gear
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GearForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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
    gear_trip_doesnt_have = Gear.objects.exclude(
        id__in=trip.gear.all().values_list('id'))
    return render(request, 'trips/detail.html', {
        'trip': trip,
        'gear': gear_trip_doesnt_have
    })


def assoc_gear(request, trip_id, gear_id):
    Trip.objects.get(id=trip_id).gear.add(gear_id)
    return redirect('detail', trip_id=trip_id)


def assoc_trip(request, trip_id, gear_id):
    Trip.objects.get(id=trip_id).gear.remove(gear_id)
    return redirect('detail', trip_id=trip_id)


class TripCreate(CreateView):
    model = Trip
    fields = ['name', 'mode', 'distance', 'nights', 'start', 'end']
    success_url = '/trips/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TripUpdate(UpdateView):
    model = Trip
    fields = ['name', 'mode', 'distance', 'nights', 'start', 'end']


class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'


class GearCreate(CreateView):
    model = Gear
    fields = ['name', 'use', 'size', 'brand', 'model', 'necessary']
    success_url = '/gear/'


class GearUpdate(UpdateView):
    model = Gear
    fields = ['name', 'use', 'size', 'brand', 'model', 'necessary']


class GearDelete(DeleteView):
    model = Gear
    success_url = '/gear/'


def signup(request):
    err_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            err_message = "That didn't work..."
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': err_message
    })
