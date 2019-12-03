from django.db import models

# Create your models here.
class City(models.Model):
    town = models.CharField(max_length=255 , unique=True)

    @property # Return all related universities
    def uni_city(self):
        return self.uni_city.all()

    def __str__(self):
        return self.town

class Speacializations(models.Model):
    pass

class Profession(models.Model):
    first_lesson = models.CharField(max_length=100)
    second_lesson = models.CharField(max_length=100)


class University(models.Model):
    city = models.ForeignKey(City , related_name='uni_city' , on_delete = models.CASCADE)
    uni_name = models.CharField(max_length=255 , unique=True)
    uni_code = models.IntegerField()
    category = models.CharField(max_length=255)
    uni_type = models.CharField(max_length=255)
    military_department = models.CharField(max_length=5)
    uni_email = models.CharField(max_length=255)
    total_grant = models.IntegerField()

    def __str__(self):
        return '{} -> {}'.format(self.city , self.uni_name)