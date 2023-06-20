import json
from datetime import datetime

def get_data():
    '''Загружает данные из файла и возвращает список словарей для дальнейшей обработки'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    '''Фильтрует данные по наличию ключа "state" в словаре и его значению "EXECUTED"'''

    #print(f"До фильтрации: { len(data) }")
    #print(f"Без ключа \"state\": { [x for x in data if 'state' not in x] }")

    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]

    #print(f"После фильтрации: {len(data)}")

    return data
