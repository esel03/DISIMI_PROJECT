from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from .models import Depend

import os
import datetime
import json


#User.objects.all().delete()


'''
def check(request):
    user = User.objects.get()
    print(user)
'''
'''
user = User.objects.get(id=1)
print(user.first_name)

django.db.utils.IntegrityError

line = Depend.objects.create(depend_field_id=1, title='Maks', views_count=1, data_create=datetime.datetime.now())

'''
def main(request):
    return render(request, 'main.html')
#django.db.utils.IntegrityError:
def registration(request):
    if request.method == "POST":
        user = User.objects.all()
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_copy = request.POST.get('password_copy')
        if password == password_copy:
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                try:
                    User.objects.get(username=username)
                except User.DoesNotExist:
                    User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    new_user = User.objects.get(username=username).id
                    response = HttpResponsePermanentRedirect('/')
                    response.set_cookie("id", new_user)
                    os.mkdir(f'neuron/templates/data_json/data_json{new_user}')
                    os.mkdir(f'neuron/templates/result_json/result_json{new_user}')
                    return response
                else:
                    return HttpResponse("Username занят")
            else:
                return HttpResponse("Email занят")
        else:
            return HttpResponse("<h1>Пароли не совпали</h1>")
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        user = User.objects.all()
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse("Во входе отказано Email")
        else:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return HttpResponse("Во входе отказано Username")
            else:
                try:
                    User.objects.get(password=password)
                except User.DoesNotExist:
                    return HttpResponse("Во входе отказано Password")
                else:
                    ex_user = User.objects.get(username=username).id
                    response = HttpResponsePermanentRedirect('/')
                    response.set_cookie("id", ex_user)
                    return response
    else:
        return render(request, 'login.html')












def short_description(request):
    id = request.COOKIES["id"]
    if request.method == "POST":
        type_product = request.POST.get('type_product')
        #name_model = request.POST.get('name_model')
        #main_func = request.POST.get('main_func')
        #color = request.POST.get('color')
        #dimensions = request.POST.get('dimensions')
        #link = request.POST.get('link')
        
        result_opros = open(f'neuron/templates/data_json/data_json{id}/data{id}.json', 'w')
        data = {"type_product": type_product} # "name_model": name_model, "main_func": main_func, "color": color, "dimensions": dimensions, "link": link

        json.dump(data, result_opros)
        result_opros.close()
        return render(request, 'confirm.html', context=data)
    else:
        return render(request, 'opros.html')

def create(request):
    id = request.COOKIES["id"]
    result_opros = open(f'neuron/templates/data_json/data_json{id}/data{id}.json', 'r')
    temp = json.load(result_opros)
    #Дальше запускается генерация текста по данным пользователя - data{id}.json
    #Пока что приводится имитация работы llama

    text_1 = [temp["type_product"], 'uspex', 'pobeda'] #присваивается значение из data{id}.json
    result_opros.close()
    result_generate = open(f'neuron/templates/result_json/result_json{id}/result{id}.json', 'w')
    json.dump({"text_1": text_1}, result_generate) #помещение результата генерации
    result_generate.close()
    #link = id

    return render(request, 'preview.html', context={"link": id})

def output(request, id):
    result_generate = open(f'neuron/templates/result_json/result_json{id}/result{id}.json', 'r')
    temp = json.load(result_generate)

    return render(request, 'result.html', context=temp)




'''
class Repression:
    def __init__(self, )

    def killed(self)
'''


















# Create your views here.
