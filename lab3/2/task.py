def find_common_participants(group1, group2, delimiter=","):
    """
    Находит общих участников среди двух групп.
    :param group1: Строка с участниками первой группы.
    :param group2: Строка с участниками второй группы.
    :param delimiter: Разделитель для списка участников (по умолчанию запятая).
    :return: Отсортированный список общих участников.
    """
    # Разбиваем строки на списки участников по разделителю
    participants_1 = set(group1.split(delimiter))
    participants_2 = set(group2.split(delimiter))

    # Находим пересечение двух множеств
    common_participants = participants_1 & participants_2

    # Возвращаем список общих участников, отсортированный в алфавитном порядке
    return sorted(common_participants)


# Данные для теста
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем функцию с разделителем "|"
common_participants = find_common_participants(
    participants_first_group, participants_second_group, delimiter="|"
)

# Вывод результата
print("Общие участники:", common_participants)
