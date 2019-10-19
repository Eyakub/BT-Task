from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *
import requests
import pprint
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from pickle import dumps


# Create your views here.
class Index(View):
    def get(self, request):
        
        for i in range(100):
            random_user = requests.get('https://randomuser.me/api/')
            random_user = random_user.json()

            gender = Gender()
            gender.type = random_user.get('results')[0]['gender']
            print(gender.type)
            gender.save()

<<<<<<< HEAD
        name = Name()
        name.title = random_user.get('results')[0]['name']['title']
        name.first = random_user.get('results')[0]['name']['first']
        name.last = random_user.get('results')[0]['name']['last']
        print(name)
        return HttpResponse('hi there')
=======
            name = Name()
            name.title = random_user.get('results')[0]['name']['title']
            name.first = random_user.get('results')[0]['name']['first']
            name.last = random_user.get('results')[0]['name']['last']
            name.save()

            street = Street()
            street.number = random_user.get('results')[0]['location']['street']['number']
            street.name = random_user.get('results')[0]['location']['street']['name']
            street.save()

            city = City()
            city.name = random_user.get('results')[0]['location']['city']
            city.save()

            state = State()
            state.name = random_user.get('results')[0]['location']['state']
            state.save()
            
            country = Country()
            country.name = random_user.get('results')[0]['location']['country']
            country.save()

            postcode = PostCode()
            postcode.number = random_user.get('results')[0]['location']['postcode']
            postcode.save()

            coordinate = Coordinate()
            coordinate.latitude = random_user.get('results')[0]['location']['coordinates']['latitude']
            coordinate.longitude = random_user.get('results')[0]['location']['coordinates']['longitude']
            coordinate.save()
            
            timezone = TimeZone()
            timezone.offset = random_user.get('results')[0]['location']['timezone']['offset']
            timezone.description = random_user.get('results')[0]['location']['timezone']['description']
            timezone.save()

            location = Location()
            location.street = get_object_or_404(Street, pk=street.id)
            location.city = get_object_or_404(City, pk=city.id)
            location.state = get_object_or_404(State, pk=state.id)
            location.country = get_object_or_404(Country, pk=country.id)
            location.postcode = get_object_or_404(PostCode, pk=postcode.id)
            location.coordinate = get_object_or_404(Coordinate, pk=coordinate.id)
            location.timezone = get_object_or_404(TimeZone, pk=timezone.id)
            location.save()

>>>>>>> 5960539a31dc93e91f0c09f0eb34e4baeb0c4f48

            email = Email()
            email.email = random_user.get('results')[0]['email']
            email.save()

            login = Login()
            login.uuid = random_user.get('results')[0]['login']['uuid']
            login.username = random_user.get('results')[0]['login']['username']
            login.password = random_user.get('results')[0]['login']['password']
            login.salt = random_user.get('results')[0]['login']['salt']
            login.md5 = random_user.get('results')[0]['login']['md5']
            login.sha1 = random_user.get('results')[0]['login']['sha1']
            login.sha256 = random_user.get('results')[0]['login']['sha256']
            login.save()

            dob = DOB()
            dob.date = random_user.get('results')[0]['dob']['date']
            dob.age = random_user.get('results')[0]['dob']['age']
            dob.save()

            registered = Registered()
            registered.date = random_user.get('results')[0]['registered']['date']
            registered.age = random_user.get('results')[0]['registered']['age']
            registered.save()

            phone = Phone()
            phone.phone_no = random_user.get('results')[0]['phone']
            phone.save()

            cell = Cell()
            cell.cell_no = random_user.get('results')[0]['cell']
            cell.save()

            rm_id = ID()
            rm_id.name = random_user.get('results')[0]['id']['name']
            rm_id.value = random_user.get('results')[0]['id']['value']
            rm_id.save()

            picture = Picture()
            picture.large = random_user.get('results')[0]['picture']['large']
            picture.medium = random_user.get('results')[0]['picture']['medium']
            picture.thumbnail = random_user.get('results')[0]['picture']['thumbnail']
            picture.save()

            nat = NAT()
            nat.nat_name = random_user.get('results')[0]['nat']
            nat.save()

        return HttpResponse('hi there')
    def post(self, request):
        pass
