import csv

positions = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv', 'w', encoding='utf-8') as wf:
    fields = ['name', 'age', 'job']
    ob_writer = csv.DictWriter(wf, fields, delimiter=';')
    ob_writer.writeheader()
    for user in positions:
        ob_writer.writerow(user)
