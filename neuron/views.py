from django.shortcuts import render
import json



def short_description(request):
    id = 12345
    if request.method == "POST":
        type_product = request.POST.get('type_product')
        #name_model = request.POST.get('name_model')
        #main_func = request.POST.get('main_func')
        #color = request.POST.get('color')
        #dimensions = request.POST.get('dimensions')
        #link = request.POST.get('link')
        
        result_opros = open(f'neuron/templates/data_json/data{id}.json', 'w')
        data = {"type_product": type_product} # "name_model": name_model, "main_func": main_func, "color": color, "dimensions": dimensions, "link": link

        json.dump(data, result_opros)
        result_opros.close()
        return render(request, 'confirm.html', context=data)
    else:
        return render(request, 'opros.html')

def create(request):
    id = 12345
    result_opros = open(f'neuron/templates/data_json/data{id}.json', 'r')
    temp = json.load(result_opros)
    #Дальше запускается генерация текста по данным пользователя - data{id}.json
    #Пока что приводится имитация работы llama

    text_1 = temp["type_product"] #присваивается значение из data{id}.json
    result_opros.close()
    result_generate = open(f'neuron/templates/result_json/result{id}.json', 'w')
    json.dump({"text_1": text_1}, result_generate) #помещение результата генерации
    result_generate.close()
    #link = id

    return render(request, 'preview.html', context={"link": id})

def output(request, id):
    result_generate = open(f'neuron/templates/result_json/result{id}.json', 'r')
    temp = json.load(result_generate)

    return render(request, 'result.html', context=temp)
























# Create your views here.
