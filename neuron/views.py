from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from .yandexGPTdemo import GENERATE_1
from .process import PROCESS
from django.contrib.auth.models import User
from .models import Depend

import os
import datetime
import json


#User.objects.all().delete()
#Depend.objects.all().delete()



def main(request):
    id_user = request.COOKIES["id"]
    print(id_user)
    return render(request, 'main.html', context={"user": id_user})



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
                    response = HttpResponseRedirect('/')
                    response.set_cookie("id", new_user, samesite=None)
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
'''
def view_login(request):
    if request.method == "POST":
        #user = User.objects.all()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, email=email, password=password)
        print(user)
        if user is not None:
            #login(request, user)
            user_id = User.objects.get(username=username).id
            response = HttpResponseRedirect('/')
            response.set_cookie("id", user_id, samesite=None)
            return response
        else:
            return HttpResponse("Во входе отказано Username")
    else:
        return render(request, 'login.html')
'''





def view_login(request):
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
                    response = HttpResponseRedirect('/')
                    response.set_cookie("id", ex_user, samesite=None)
                    return response
    else:
        return render(request, 'login.html')


def exit(request):
    response = HttpResponseRedirect('/room/')
    response.set_cookie("id", 0000,samesite=None)
    return response

    '''
    if request.COOKIES.get("id"):
        response = HttpResponse('Out Account')
        response.delete_cookie("id")
        return response
    else:
        return HttpResponse('Yet out Account')
    '''




def room(request):
    id_user = request.COOKIES["id"]
    local_var = Depend.objects.filter(depend_field_id=id_user, views_count=1)
    return render(request, 'room.html', context={"id_user": id_user, "lang": list(local_var)})




#Depend.objects.create(depend_field_id=7, title='name', views_count=1, data_create=datetime.datetime.now())



def short_description(request):
    id_user = request.COOKIES["id"]
    if request.method == "POST":
        name = request.POST.get('name')
        
        try:
            Depend.objects.get(depend_field_id=id_user, title=name)
        except Depend.DoesNotExist:
            Depend.objects.create(depend_field_id=id_user, title=name, data_create=datetime.datetime.now())
            id_depend = Depend.objects.get(depend_field_id=id_user, title=name).id
            result_opros = open(f'neuron/templates/data_json/data_json{id_user}/data{id_depend}.json', 'w')
            data = {"name": name} # "name_model": name_model, "main_func": main_func, "color": color, "dimensions": dimensions, "link": link

            json.dump(data, result_opros, ensure_ascii=False)
            result_opros.close()
            response = HttpResponsePermanentRedirect('/short_description/confirm')
            response.set_cookie("name", name, samesite=None)
            return response
        else:
            return render(request, 'opros.html', context={"error": 1})
    else:
        return render(request, 'opros.html', context={"error": 0})


def confirm(request):
    id_user = request.COOKIES["id"]
    name = request.COOKIES["name"]
    id_depend = Depend.objects.get(depend_field_id=id_user, title=name).id

    result_opros = open(f'neuron/templates/data_json/data_json{id_user}/data{id_depend}.json', 'r')
    temp = json.load(result_opros)
    return render(request, 'confirm.html', context=temp)






def create(request):
    id_user = request.COOKIES["id"]
    name = request.COOKIES["name"]
    id_depend = Depend.objects.get(depend_field_id=id_user, title=name).id
    result_opros = open(f'neuron/templates/data_json/data_json{id_user}/data{id_depend}.json', 'r')
    temp = json.load(result_opros)
    #Дальше запускается генерация текста по данным пользователя - data{id}.json
    #Пока что приводится имитация работы llama

    first_gen = GENERATE_1(temp) #присваивается значение из data{id}.json
    result_first_gen = PROCESS(id_user, id_depend, first_gen)
    result_opros.close()
    result_generate = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'w')
    json.dump({"result_first_gen": result_first_gen}, result_generate, ensure_ascii=False) #помещение результата генерации
    result_generate.close()
    Depend.objects.filter(depend_field_id=id_user).update(views_count=True)

    return render(request, 'preview.html', context={"id_user": id_user, "id_depend": id_depend})

def output(request, id_user, id_depend):
    result_generate = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'r')
    temp = json.load(result_generate)

    return render(request, 'result.html', context=temp)























# Create your views here.
