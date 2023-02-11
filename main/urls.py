from django.urls import path
from . import views  # importing our view file

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('trips/', views.trip_index, name='index'),
    path("gear/", views.gear, name="gear"),
    path('trips/<int:trip_id>/', views.trip_detail, name='detail'),
    path('gear/<int:gear_id>/', views.gear_detail, name='gear_detail'),
    path('trips/create/', views.TripCreate.as_view(), name='trip_create'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trip_delete'),
    path('gear/create/', views.GearCreate.as_view(), name='gear_create'),
    path('gear/<int:pk>/update/', views.GearUpdate.as_view(), name='gear_update'),
    path('gear/<int:pk>/delete/', views.GearDelete.as_view(), name='gear_delete'),
]
