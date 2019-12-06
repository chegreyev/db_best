from django.db import models 

class City(models.Model):

    city_name = models.CharField(max_length=100 , primary_key = True)

    @property
    def universities(self):
        return universities.all()

    def __str__(self):
        return format(self.city_name)

class University(models.Model):

    location = models.ForeignKey(City , related_name = 'universities' , on_delete = models.CASCADE)
    university_name = models.CharField(max_length = 255 , primary_key = True)
    university_code = models.IntegerField(null = True , blank = True)
    university_category = models.CharField(max_length= 255 , default = 'State' , null=True)
    university_type = models.CharField(max_length= 255 , default = 'University' , null = True)
    university_email = models.CharField(max_length=100 , null =True)
    university_site = models.CharField(max_length=100 , null = True)
    military_dep = models.CharField(max_length=10 , default = 'No')

    @property
    def professions(self):
        return profession.all()

    def __str__(self):
        return '{} -> {}'.format(self.location , self.university_name)

    
class Profession(models.Model):

    university = models.ForeignKey(University , related_name = 'professions' , on_delete = models.CASCADE)
    prof_title = models.CharField(max_length=255)
    first_lesson = models.CharField(max_length=100)
    second_lesson = models.CharField(max_length=100)
    total_grant = models.IntegerField(null = True)
    full_kz = models.IntegerField(null = True)
    full_ru = models.IntegerField(null = True)
    full_en = models.IntegerField(null= True)
    shortened_kz = models.IntegerField(null = True)
    shortened_ru = models.IntegerField(null =True)

    def __str__(self):
        return '{}'.format(self.prof_title)

