def autoreplace_unique(text, replacements):
    # Создаем временные метки для замены
    temp_text = text
    for old_char, new_char in replacements.items():
        temp_text = temp_text.replace(old_char, new_char)
    return temp_text

# Чтение данных из файла
with open('data.txt', 'r', encoding="utf8") as file:
    data = file.read()

# Определяем замены
replacements_1 = {
    "У": " "
}

# Выполняем первую замену
data = autoreplace_unique(data, replacements_1)

# Сохраняем промежуточный результат

# Определяем вторые замены
replacements_2 = {
    " ": "1234"
}

# Перед второй заменой временно заменим "М" на уникальный символ (например, "X")
data = data.replace(" ", "*")

# Выполняем вторую замену
data = autoreplace_unique(data, replacements_2)

# Заменяем временный символ обратно на "М"
data = data.replace("*", " ")



# Выводим финальный результат
print(data)