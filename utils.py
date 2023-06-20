import json
from datetime import datetime

def get_data():
    '''Загружает данные из файла и возвращает список словарей для дальнейшей обработки'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

