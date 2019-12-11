from rest_framework import serializers
from .models import * 

class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['prof_title' , 'first_lesson' , 'second_lesson' , 'total_grant' , 'full_kz' , 'full_ru' , 'full_en' , 'shortened_kz' , 'shortened_ru']

class UniversitySerializer(serializers.ModelSerializer):
    professions = ProfessionsSerializer(many = True)

    class Meta:
        model = University
        fields = ['university_name' , 'university_code' , 'university_category' , 'university_type' , 'military_dep' ,'university_email' , 'university_site' , 'professions']


class CitySerializer(serializers.ModelSerializer):
    universities = UniversitySerializer(many = True)

    class Meta:
        model = City
        fields = ['city_name' , 'universities']

class TUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TUser
        fields = ['user_id' , 'user_login' , 'password']

class TUserRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TUserRating
        fields = ['user_id' , 'profession' , 'university_name' , 'university_rating']