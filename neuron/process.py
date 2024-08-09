import json
#from yandexGPTdemo import generate

def PROCESS(id_user, id_depend, variable):
    data = eval(variable)
    result = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'w')
    json.dump(data, result, ensure_ascii=False)
    result.close()

    
    main = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'r')
    temp = json.load(main)
    main.close()

    file = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'w')
    json.dump(temp["result"], file, ensure_ascii=False)
    file.close()

    
    main_1 = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'r')
    temp_1 = json.load(main_1)
    main_1.close()

    file_1 = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'w')
    json.dump(temp_1["alternatives"], file_1, ensure_ascii=False)
    file_1.close()


    main_2 = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'r')
    temp_2 = json.load(main_2)
    main_2.close()

    file_2 = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'w')
    json.dump(temp_2[0], file_2, ensure_ascii=False)
    file_2.close()


    main_3 = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'r')
    temp_3 = json.load(main_3)
    main_3.close()

    file_3 = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'w')
    json.dump(temp_3["message"], file_3, ensure_ascii=False)
    file_3.close()


    main_4 = open(f'neuron/templates/result_json/result_json{id_user}/result{id_depend}.json', 'r')
    temp_4 = json.load(main_4)
    main_4.close()
    return temp_4["text"]

