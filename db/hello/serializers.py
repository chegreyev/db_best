from rest_framework import serializers
from .models import * 

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id' , 'spec_code' , 'spec_title' , 'total_grant' , 'full_kz' , 'full_rus' , 'full_eng' , 'shortened_kz' ,'shortened_ru']

class ProfesionSerializer(serializers.ModelSerializer):
    profession_specializations = SpecializationSerializer(many = True)

    class Meta:
        model = Profesion
        fields = ['prof_title' , 'first_lesson' , 'second_lesson' , 'profession_specializations']

class UniversitySerializer(serializers.ModelSerializer):
    university_professions = ProfesionSerializer(many = True)

    class Meta:
        model = University
        fields = ['id' , 'university_name' , 'university_code' , 'university_category' , 'university_type' , 'military_dep' ,'university_email' , 'university_site' , 'university_professions']


class CitySerializer(serializers.ModelSerializer):
    universities = UniversitySerializer(many = True)

    class Meta:
        model = City
        fields = ['city_name' , 'universities']

