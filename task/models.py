from django.db import models


# Create your models here.
class Gender(models.Model):
    type = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.type


class Name(models.Model):
    title = models.CharField(max_length=20, null=True)
    first = models.CharField(max_length=100, null=True)
    last = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.first


class Street(models.Model):
    number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=191, null=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class PostCode(models.Model):
    number = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.number


class Coordinate(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)


class TimeZone(models.Model):
    offset = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True)


class Email(models.Model):
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.email


class Login(models.Model):
    uuid = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    salt = models.CharField(max_length=255, null=True)
    md5 = models.CharField(max_length=255, null=True)
    sha1 = models.CharField(max_length=255, null=True)
    sha256 = models.CharField(max_length=255, null=True)


class DOB(models.Model):
    date = models.DateTimeField()
    age = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.date


class Registered(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.date


class Phone(models.Model):
    phone_no = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.phone_no


class Cell(models.Model):
    cell_no = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.cell_no


class ID(models.Model):
    name = models.CharField(max_length=150, null=True)
    value = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.name


class Location(models.Model):
    street = models.ForeignKey(Street, related_name='locations', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='locations', on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name='locations', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='locations', on_delete=models.CASCADE)
    postcode = models.ForeignKey(PostCode, related_name='locations', on_delete=models.CASCADE)
    coordinate = models.ForeignKey(Coordinate, related_name='locations', on_delete=models.CASCADE)
    timezone = models.ForeignKey(TimeZone, related_name='locations', on_delete=models.CASCADE)

    def __str__(self):
        return self.city.name + self.country.name


class Picture(models.Model):
    large = models.CharField(max_length=300, null=True)
    medium = models.CharField(max_length=300, null=True)
    thumbnail = models.CharField(max_length=300, null=True)


class NAT(models.Model):
    nat_name = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.nat_name
