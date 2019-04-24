from django.shortcuts import render
from django.http import JsonResponse
import string
from random import *
from django.utils import timezone


def create_random_code():
    return randint(1, 100)


def create_random_age():
    return randint(15, 50)


def create_random_string():
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(10))


def create_json_random(request):
    data = {

        'name': create_random_string(),
        'family': create_random_string(),
        'age': create_random_age(),
        'code': create_random_code(),
        'time': timezone.now()
    }
    return JsonResponse(data, safe=False)
# Create your views here.
