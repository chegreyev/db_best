from rest_framework import serializers
from .models import * 


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    uni_city = UniversitySerializer(many = True)

    class Meta:
        model = City
        fields = ['id' , 'town' , 'uni_city']
