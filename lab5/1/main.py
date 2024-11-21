import json


def task() -> float:
    # Открываем файл JSON для чтения данных
    with open('Input.json', 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений "score" и "weight"
    total_sum = sum(item['score'] * item['weight'] for item in data)

    # Округляем результат до 3 десятичных знаков
    return round(total_sum, 3)


# Вывод результата
print(task())
