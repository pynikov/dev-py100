# Функция для поиска индекса товара
def find_item_index(items, item):
    """
    Находит индекс первого вхождения товара в списке.
    :param items: Список товаров.
    :param item: Товар, который нужно найти.
    :return: Индекс первого вхождения товара или None, если товар не найден.
    """
    if item in items:
        return items.index(item)  # Возвращаем индекс первого вхождения
    return None  # Возвращаем None, если товар не найден

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Проверяем для каждого товара
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
