from django.urls import path
from .views import *

urlpatterns = [
    path('city/' , CityView.as_view() , name = 'city_list'),
    path('university/' , UniversityView.as_view() , name = 'university_list'),
]