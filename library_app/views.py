from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime


def about_time(request):
    a = datetime.now().replace(microsecond=0)
    if request.method == "GET":
        return HttpResponse(a)


def about_pets(request):
    pet_name = "Барбос"
    pet_age = 12
    pet_birthday = '12.02.2012'
    if request.method == 'GET':
        print_result = f"{pet_name}\n{pet_age}\n{pet_birthday}"
        return HttpResponse(print_result)

