import re

#z1
print("##################Z1#########################")
with open('task1-en.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Слова с дефисом
hyphenated_words = re.findall(r'\b\w+-\w+\b', text)

# Информация в круглых скобках
parentheses_content = re.findall(r'\([^()]*\)', text)

print("Слова с дефисом:", hyphenated_words)
print("Информация в скобках:", parentheses_content)

#z2
print()
print("##################Z2#########################")
with open('task2.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Ссылки в домене .com
com_links = re.findall(r'https?://[\w.-]+\.com\b', html)

print("Ссылки в домене .com:", com_links)

print()
print("##################Z3#########################")
import re
import csv

with open('task3.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Извлечение данных
ids = re.findall(r'\b\d+\b', data)
surnames = re.findall(r'\b[А-ЯA-Z][а-яa-z]+\b', data)
emails = re.findall(r'[\w.-]+@[\w.-]+\.[a-z]{2,}', data)
dates = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', data)
websites = re.findall(r'https?://[\w.-]+\.[a-z]{2,}', data)

# Запись в CSV
with open('task3_normalized.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Фамилия', 'Email', 'Дата регистрации', 'Сайт'])
    for i in range(len(ids)):
        writer.writerow([
            ids[i] if i < len(ids) else '',
            surnames[i] if i < len(surnames) else '',
            emails[i] if i < len(emails) else '',
            dates[i] if i < len(dates) else '',
            websites[i] if i < len(websites) else '',
        ])

print("Данные сохранены в 'task3_normalized.csv'")