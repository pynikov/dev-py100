import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = list(csv_reader)  # Преобразовываем прочитанные данные в список словарей

    # Сериализуем данные в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    task()

    # Читаем и печатаем содержимое созданного JSON файла
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
