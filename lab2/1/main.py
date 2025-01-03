money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов


# Переменная для подсчета количества месяцев
months = 0

# Пока есть деньги в подушке безопасности
while money_capital >= 0:
    # Вычитаем текущие траты из подушки безопасности
    money_capital -= spend - salary  # Бюджет = подушка - (траты - зарплата)

    # Если деньги закончились, выходим из цикла
    if money_capital < 0:
        break

    # Увеличиваем счетчик месяцев
    months += 1

    # Увеличиваем расходы на 5% (рост цен)
    spend *= (1 + increase)

# Выводим результат
print("Количество месяцев, которое можно протянуть без долгов:", months)
