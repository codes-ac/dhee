from weather import views
from django.urls import path
from .views import WeatherApiView

urlpatterns = [

    path('weather_api/', WeatherApiView.as_view(), name="weather_api")
    ]