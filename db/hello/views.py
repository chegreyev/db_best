from django.shortcuts import render
from rest_framework import generics
from .serializers import * 
from .models import * 

# Create your views here.
class UniversityView(generics.ListAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()

class CityView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class ProfesionView(generics.ListAPIView):
    serializer_class = ProfesionSerializer
    queryset = Profesion.objects.all()

class SpecializationView(generics.ListAPIView):
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()
