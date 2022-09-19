# Генератор пароля
# Выбор длины пароля от минимального 4 до 128
# Выбор англисукого алфавита, цифр и символов
# Не повторяемость символов

# Импорт генерация случайных чисел (модуль random)
import random

# Создаем списки
pass_little = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
pass_big = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
pass_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
pass_symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[',
    ']', '{', '}', ';', ':', '/', '?', '.', '>', '<'
]
user_password = []

print('''Выберите длину пароля. Минимальная длина 4 символа,
    максимальная длина 128 символов.
        ''')

# Проверка длина пароля
for _ in range(5):  # Проверяем 5 раз
    pass_length = int(input("Длина: "))
    if pass_length > 128 or pass_length < 4:
        print('Минимальная длина пароля 4 символа, максимальная 128')
        pass_length = 4
    else:
        break

print('''Пароль состоит из символов:
        строчных (abc...)   - 1
        прописных (ABC...), строчных  - 2
        чисел (123...),  прописных, строчных - 3
        специальные (! @ # ...), чисел, прописных, строчных - 4
        ''')
pass_type = int(input('Выберите состав: '))

# Выбор состава
if pass_type == 1:
    pass_base = pass_little
elif pass_type == 2:
    pass_base = pass_little + pass_big
elif pass_type == 3:
    pass_base = pass_little + pass_big + pass_numbers
else:
    pass_base = pass_little + pass_big + pass_numbers + pass_symbols

# Генерация пароля
for i in range(pass_length):
    user_password.append(random.choice(pass_base))

user_password = ''.join(user_password)
print('Пароль: ', user_password)

# Для показа термина после расчетов
print()
input('Для закрытия нажмите Enter')