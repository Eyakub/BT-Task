from django.db import models
from

# Create your models here.
class Gender(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return str(self.type)


class Name(models.Model):
    title = models.CharField(max_length=20)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)

    def __str__(self):
        return str(self.first)


class Location(models.Model):
    street = models.ForeignKey(Street, related_name='locations', on_delete=models.SET_NULL)
    city = models.ForeignKey(City, related_name='locations', on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name='locations', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='locations', on_delete=models.CASCADE)
    postcode = models.ForeignKey(PostCode, related_name='locations', on_delete=models.CASCADE)
    coordinate = models.ForeignKey(Coordinate, related_name='locations', on_delete=models.CASCADE)
    timezone = models.ForeignKey(TimeZone, related_name='locations', on_delete=models.CASCADE)


class Street(models.Model):
    number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)


class City(models.Model):
    pass


class State(models.Model):
    pass


class Country(models.Model):
    pass


class PostCode(models.Model):
    pass


class Coordinate(models.Model):
    pass


class TimeZone(models.Model):
    pass


class Email(models.Model):
    pass


class Login(models.Model):
    pass


class DOB(models.Model):
    pass


class Registered(models.Model):
    pass


class Phone(models.Model):
    pass


class Cell(models.Model):
    pass


class ID(models.Model):
    pass


class Picture(models.Model):
    large = models.CharField(max_length=300)
    medium = models.CharField(max_length=300)
    thumbnail = models.CharField(max_length=300)


class NAT(models.Model):
    pass
