from django.db import models

# Create your models here.
class City(models.Model):
    town = models.CharField(max_length=255 , unique=True)

    @property # Return all related universities
    def uni_city(self):
        return self.uni_city.all()

    def __str__(self):
        return self.town

class University(models.Model):
    city = models.ForeignKey(City , related_name='uni_city' , on_delete = models.CASCADE)
    uni_name = models.CharField(max_length=255 , unique=True)
    uni_code = models.IntegerField()
    category = models.CharField(max_length=255)
    uni_type = models.CharField(max_length=255)
    military_department = models.CharField(max_length=5)
    uni_email = models.CharField(max_length=255)
    total_grant = models.IntegerField()
    uni_site = models.CharField(max_length=255)

    @property
    def univer_prof(self):
        return self.univer_prof.all()

    def __str__(self):
        return '{} -> {}'.format(self.city , self.uni_name)

class Profession(models.Model):
    code = models.CharField(max_length=9)
    univer = models.ForeignKey(University , related_name='univer_prof' , on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    first_lesson = models.CharField(max_length=100)
    second_lesson = models.CharField(max_length=100)

    @property
    def spec_prof(self):
        return self.spec_prof.all()

    def __str__(self):
        return '{} -> {}'.format(self.code , self.title)

class Specialization(models.Model):
    prof = models.ForeignKey(Profession , related_name='spec_prof' , on_delete = models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.title)