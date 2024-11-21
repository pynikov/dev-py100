# TODO Найдите количество книг, которое можно разместить на дискете

# Данные задачи
disk_capacity_mb = 1.44  # Объём дискеты в мегабайтах
pages_per_book = 100     # Количество страниц в книге
lines_per_page = 50      # Количество строк на странице
chars_per_line = 25      # Количество символов в строке
bytes_per_char = 4       # Объём одного символа в байтах

# Перевод объёма дискеты из мегабайтов в байты
disk_capacity_bytes = int(disk_capacity_mb * 1024 * 1024)

# Расчёт объёма одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Вычисление количества книг, помещающихся на дискету (целочисленное деление)
books_on_disk = disk_capacity_bytes // book_size_bytes

# Вывод результата
print("Количество книг, помещающихся на дискету:", books_on_disk)
