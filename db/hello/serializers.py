from rest_framework import serializers
from .models import * 

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id' , 'title']

class ProfessionSerializer(serializers.ModelSerializer):
    spec_prof = SpecializationSerializer(many = True)

    class Meta:
        model = Profession
        fields = ['id' , 'code' , 'title' , 'first_lesson' , 'second_lesson' , 'spec_prof']

class UniversitySerializer(serializers.ModelSerializer):
    univer_prof = ProfessionSerializer(many = True)

    class Meta:
        model = University
        fields = ['id' , 'uni_name' , 'uni_code' , 'category' , 'uni_type' , 'military_department' ,'uni_email' , 'uni_site' ,'total_grant' , 'univer_prof']


class CitySerializer(serializers.ModelSerializer):
    uni_city = UniversitySerializer(many = True)

    class Meta:
        model = City
        fields = ['id' , 'town' , 'uni_city']

