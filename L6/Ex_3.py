'''
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''

from itertools import zip_longest

users_dict = {}
with open('users.csv', encoding='utf-8') as users_file:
    with open('hobby.csv', encoding='utf-8') as hobbies_file:
        for users, hobbies in zip_longest(users_file, hobbies_file, fillvalue='None'):
            users_dict.setdefault(users.rstrip(), hobbies.rstrip())
with open('dict_of_hobbies.txt', 'w', encoding='utf-8') as full_file:
    for k, v in users_dict.items():
        if k != 'None':
            full_file.writelines(f'{k}: {v}\n')
        else:
            exit(1)