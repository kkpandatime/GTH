'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
'''

import re

def email_parse(email):
    VALID_EMAIL = re.compile((r'^[a-zA-Z0-9_.+-]+'
                              r'@'
                             r'[a-zA-Z0-9-]{3,}\.[a-zA-Z0-9-.]{2,}$'))
    data_dict = {}
    try:
        if VALID_EMAIL.match(email):
            login, domain = email.split('@')
            data_dict['username'] = login
            data_dict['domain'] = domain
            return data_dict
        else:
            raise ValueError
    except ValueError:
        return print(f'ValueError: wrong email: {email}')


if __name__ == '__main__':
    print(email_parse(input('Enter email: ')))