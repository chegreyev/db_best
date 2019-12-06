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

class ProfessionView(generics.ListAPIView):
    serializer_class = ProfessionsSerializer
    queryset = Profession.objects.all()
    
