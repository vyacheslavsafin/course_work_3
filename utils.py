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


def encode_bill_info(bill_info):
    """Шифрует номера счетов и карт"""
    bill_info = bill_info.split()
    bill, info = bill_info[-1], " ".join(bill_info[:-1])
    if len(bill) == 16:
        bill = f"{bill[:4]} {bill[4:6]}** **** {bill[-4:]}"
    else:
        bill = f"**{bill[-4:]}"

    to = f"{info} {bill}"
    return to


def get_formatted_data(data):
    """Приводит дату, описание и отправителя в нужный формат"""
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

        description = row["description"]

        if "from" in row:
            sender = encode_bill_info(row["from"])
            sender = f"{ sender } -> "
        else:
            sender = ""

        to = encode_bill_info(row['to'])

        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender}{to}
{operations_amount}""")
    return formatted_data