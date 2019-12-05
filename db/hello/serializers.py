from rest_framework import serializers
from .models import * 

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id' , 'spec_code' , 'spec_title' , 'total_grant' , 'full_kz' , 'full_rus' , 'full_eng' , 'shortened_kz' ,'shortened_ru']

class ProfesionSerializer(serializers.ModelSerializer):
    spec_prof = SpecializationSerializer(many = True)

    class Meta:
        model = Profesion
        fields = ['id' , 'prof_title' , 'first_lesson' , 'second_lesson' , 'spec_prof']

class UniversitySerializer(serializers.ModelSerializer):
    univer_prof = ProfesionSerializer(many = True)

    class Meta:
        model = University
        fields = ['id' , 'university_name' , 'university_code' , 'university_category' , 'university_type' , 'military_dep' ,'university_email' , 'university_site' , 'univer_prof']


class CitySerializer(serializers.ModelSerializer):
    location = UniversitySerializer(many = True)

    class Meta:
        model = City
        fields = ['id' , 'city_name' , 'location']

