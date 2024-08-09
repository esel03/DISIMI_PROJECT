import requests
#from curl_cffi import requests
import json

def GENERATE_1(temp):
    prompt = {
        "modelUri": "gpt://b1g7in2c2dp5md2dei6m/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
            "text": "Ты Пасько."
            },
            {
                "role": "user",
            "text": f"Обыграй это - {temp["name"]} десятью словами."
            },
            {
                "role": "assistant",
            "text": "Я поведую тебе анекдот:"
            },
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNxvY-FnLp3ZX2L5yk8LjelO89edaWFRmhAX21"
    }
    #session = requests.Session()
    response = requests.post(url, headers=headers, json=prompt)
    result = response
    return result.text




