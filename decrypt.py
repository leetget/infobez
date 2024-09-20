def autoreplace_unique(text, replacements):
    for old_char, new_char in replacements.items():
        # Заменяем только те символы, которые еще не были заменены
        if old_char in text:
            text = text.replace(old_char, new_char)
    return text

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
with open('data_step1.txt', 'w', encoding="utf8") as file:
    file.write(data)

# Определяем вторые замены
replacements_2 = {
    " ": "й"
}

# Выполняем вторую замену
data = autoreplace_unique(data, replacements_2)

# Сохраняем финальный результат
with open('data_final.txt', 'w', encoding="utf8") as file:
    file.write(data)

# Выводим финальный результат
print(data)