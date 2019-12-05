from django.db import models 

class City(models.Model):

    city_name = models.CharField(max_length=100)

    @property
    def location(self):
        return location.all()

    def __str__(self):
        return format(self.city_name)

class University(models.Model):

    location = models.ForeignKey(City , related_name = 'location' , on_delete = models.CASCADE)
    university_name = models.CharField(max_length = 255)
    university_code = models.IntegerField()
    university_category = models.CharField(max_length= 255 , default = 'State')
    university_type = models.CharField(max_length= 255 , default = 'University')
    university_email = models.CharField(max_length=100)
    university_site = models.CharField(max_length=100)
    military_dep = models.CharField(max_length=10 , default = 'No')

    @property
    def univer_prof(self):
        return univer_prof.all()

    def __str__(self):
        return '{} -> {}'.format(self.location , self.university_name)

    
class Profesion(models.Model):

    university = models.ForeignKey(University , related_name = 'univer_prof' , on_delete = models.CASCADE)
    prof_title = models.CharField(max_length = 255)
    first_lesson = models.CharField(max_length = 100)
    second_lesson = models.CharField(max_length = 100)

    @property
    def spec_prof(self):
        return spec_prof.all()

    def __str__(self):
        return '{} -> {}'.format(self.university ,self.prof_title)

class Specialization(models.Model):
    prof = models.ForeignKey(Profesion , related_name = 'spec_prof' , on_delete = models.CASCADE)

    spec_code = models.CharField(max_length=10)
    spec_title = models.CharField(max_length = 255)
    total_grant = models.IntegerField()
    full_kz = models.IntegerField()
    full_rus = models.IntegerField()
    full_eng = models.IntegerField()
    shortened_kz = models.IntegerField()
    shortened_ru = models.IntegerField()

    def __str__(self):
        return '{} -> {}'.format(self.prof , self.spec_title)

