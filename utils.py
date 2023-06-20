import json
from datetime import datetime

def get_data():
    '''Загружает данные из файла и возвращает список словарей для дальнейшей обработки'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    '''Фильтрует данные по наличию ключа "state" в словаре и его значению "EXECUTED"'''

    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_values(data, count_last_values):
    '''Сортирует данные по дате и выводит последние пять транзакций'''

    def key_sort(x):
        return x["date"]

    data = sorted(data, key=key_sort, reverse=True)

    data = data[:count_last_values]
    return data





def get_formatted_data(data):
    """Приводит дату, описание и отправителя в нужный формат"""
    formatted_data = []
    for row in data:
        print(f"Дата: {row['date']}")
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        print(f"Дата: {date}")

        description = row["description"]
        print(f"Описание: {description}")

        if "from" in row:
            sender = encode_bill_info(row['from'])
            sender = f"{sender} -> "
        else:
            sender = ""

        to = encode_bill_info(row['to'])

        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender} {to}
{operations_amount}""")
    return formatted_data