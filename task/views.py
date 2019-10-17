from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *
import requests
import pprint

# Create your views here.


class Index(View):
    def get(self, request):
        random_user = requests.get('https://randomuser.me/api/')
        random_user = random_user.json()

        gender = Gender()
        gender.type = random_user.get('results')[0]['gender']

        name = Name()
        name.title = random_user.get('results')[0]['name']['title']
        name.first = random_user.get('results')[0]['name']['first']
        name.last = random_user.get('results')[0]['name']['last']

        return HttpResponse('hi there')

    def post(self, request):
        pass
