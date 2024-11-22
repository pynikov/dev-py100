import random
import time

map_ = [i for i in range(1, 10)]

VICTORY = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


def print_map():
    for i in range(3):
        print(f'| {map_[i * 3]} | {map_[i * 3 + 1]} | {map_[i * 3 + 2]} |')


def check_number(s):
    try:
        number = int(s)
        if number in map_:
            return number
        else:
            print('Неправильная позиция или место занято!')
    except ValueError:
        print('Вы ввели не число')
    return -1


def step_in_map(n, symb):
    ind = map_.index(n)
    map_[ind] = symb


def ai_step():
    data = [el for el in map_ if isinstance(el, int)]
    return random.choice(data)


def get_result():
    for line in VICTORY:
        if map_[line[0]] == map_[line[1]] == map_[line[2]]:
            return map_[line[0]]
    return ''


def game():
    name1 = input('Игрок 1, введите ваше имя: ')
    game_mode = input('Хотите играть против другого игрока или компьютера? Введите "человек" или "компьютер": ')
    name2 = "Компьютер" if game_mode.lower() == "компьютер" else input('Игрок 2, введите ваше имя: ')

    count_ = 0
    while True:
        count_ += 1
        print_map()
        current_player = name1 if count_ % 2 != 0 else name2
        symbol = 'X' if count_ % 2 != 0 else '0'

        if current_player == "Компьютер":
            print('Ход компьютера!')
            time.sleep(1)
            number = ai_step()
            step_in_map(number, symbol)
        else:
            s = input(f'{current_player}, введите номер клетки: ')
            number = check_number(s)
            if number == -1:
                count_ -= 1
                continue
            step_in_map(number, symbol)

        win = get_result()
        if win:
            print(f'{current_player} победил!')
            break
        if count_ == 9:
            print('Ничья!')
            break


if __name__ == "__main__":
    game()
