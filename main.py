# Генератор безопасных паролей
import random


def generate_password(length, chars):
    """
    Создаем случайный пароль на основе выбранной длина и набора символов
    Аргументы:
    length - Длина каждого пароля
    symbols - Список символов используемых для создания пароля
    """
    user_password = ""  # Новый список для пароля
    for _ in range(length):
        user_password += random.choice(chars)
    print("Пароль: ", user_password)


# Создайте строковые константы
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

print("Генератор безопасных паролей")
# Запрос на количество генерируемых паролей
count = int(input("Выберите количество паролей: "))
if count <= 0:  # Если количество паролей меньше 1
    count = 1
    print("Количество паролей не может быть меньше 1")

# Запрос на длину пароля
length = int(input("Выберите длину пароля: "))

# Выбор состава символов для пароля
while True:  # Основной цикл
    chars = ""  # Пустая переменная для символов
    print("Выберете состав пароля")
    pass_type = str(input("- Пароль включает строчные символов (abc...)? (Д / Н): "))
    if pass_type == "Д" or pass_type == "д":
        chars += lowercase_letters

    pass_type = str(input("- Пароль включает прописные символов (ABC...)? (Д / Н): "))
    if pass_type == "Д" or pass_type == "д":
        chars += uppercase_letters

    pass_type = str(input("- Пароль включает числа (123...)? (Д / Н): "))
    if pass_type == "Д" or pass_type == "д":
        chars += digits

    pass_type = str(
        input("- Пароль включает специальные символы (! @ # ...)? (Д / Н): ")
    )
    if pass_type == "Д" or pass_type == "д":
        chars += punctuation

    if chars == "":  # Проверяем выбрали символы
        print("Не выбраны символы для пароля!")
        continue

    similar_symbols = input("Исключать ли неоднозначные символы il1Lo0O? (Д / Н): ")
    if similar_symbols == "Д" or similar_symbols == "д":
        for c in "il1Lo0O":
            chars = chars.replace(c, "")

    for _ in range(count):  # Цикл по количеству паролей
        generate_password(length, chars)  # Создаем пароль

    # Запрос на выход
    exit = input("Хотите закрыть программу? (Д / Н)) ")
    if exit == "Н" or exit == "н":
        continue
    else:
        break
