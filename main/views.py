from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Trip, Gear, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GearForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid

S3_BASE_URL = 'http://s3.us-east-2.amazonaws.com/'
BUCKET = 'routr-bucket'


def home(request):
    return render(request, 'index.html', context={})


def about(request):
    return render(request, 'about.html')


@login_required
def gear(request):
    gears = Gear.objects.filter(user=request.user)
    return render(request, 'gear/index.html', {'gears': gears})


@login_required
def gear_detail(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    gear_form = GearForm()
    return render(request, 'gear/detail.html', {'gear': gear, 'gear_form': gear_form})


@login_required
def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/index.html', {'trips': trips})


@login_required
def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    gear_trip_doesnt_have = Gear.objects.exclude(
        id__in=trip.gear.all().values_list('id'))
    return render(request, 'trips/detail.html', {
        'trip': trip,
        'gear': gear_trip_doesnt_have
    })


def add_photo(request, trip_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, trip_id=trip_id)
            photo.save()
        except Exception as error:
            print("Upload didn't quite work")
            print(error)
    return redirect('detail', trip_id=trip_id)


def assoc_gear(request, trip_id, gear_id):
    Trip.objects.filter(user=request.user).get(id=trip_id).gear.add(gear_id)
    return redirect('detail', trip_id=trip_id)


def assoc_trip(request, trip_id, gear_id):
    Trip.objects.get(id=trip_id).gear.remove(gear_id)
    return redirect('detail', trip_id=trip_id)


class TripCreate(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ['name', 'mode', 'distance', 'nights', 'start', 'end']
    success_url = '/trips/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ['name', 'mode', 'distance', 'nights', 'start', 'end']


class TripDelete(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = '/trips/'


class GearCreate(LoginRequiredMixin, CreateView):
    model = Gear
    fields = ['name', 'use', 'size', 'brand', 'model', 'necessary', ]
    success_url = '/gear/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GearUpdate(LoginRequiredMixin, UpdateView):
    model = Gear
    fields = ['name', 'use', 'size', 'brand', 'model', 'necessary']


class GearDelete(LoginRequiredMixin, DeleteView):
    model = Gear
    success_url = '/gear/'


def signup(request):
    error_message = ''
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
        'error': error_message
    })
