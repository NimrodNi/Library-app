from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from datetime import datetime
from . import models


# получение id и получение полной информации о фильме
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.BookModel, id=id)
        context = {
            'book_id': book_id,
        }
        return render(request, template_name='show_detail.html', context=context)


# не полная информация
def book_list_view(request):
    if request.method == "GET":
        # query запрос что мы хотим видеть на html странице
        book_list = models.BookModel.objects.all().order_by('-id')
        # context_object_name = нужен для передачи данных на html шаблон в виде ключа
        context = {
            'book_list': book_list,
        }
        return render(request, template_name='show.html', context=context)

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

