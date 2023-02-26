# Вариант 1
# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».
import re

# Поиск фамилий
surname = re.compile(r"[А-ЯЁ]\S+(?=\s[А-ЯЁ]\.[А-ЯЁ])")
# Поиск слова "роман"
roman = re.compile("[Рр]оман(?=\s)")

f = open('writer.txt', encoding='UTF-8')
text = f.read()
surnameList = surname.findall(text)
f.close()

f = open('newWriter.txt', 'w+', encoding='UTF-8')
# Запись текста с подменой слова "роман" на слово "произведение"
f.write(re.sub(roman, 'произведение', text))
f.close()

print("Фамилии писателей:", surnameList)
print("Их количество: ", len(surnameList))
