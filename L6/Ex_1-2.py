'''
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов;
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

SERVERFILE = 'nginx_logs.txt'
def logs_parse(SERVERFILE):

    with open(SERVERFILE) as file:
        for line in file:
            addr = line.split('- -')[0]
            type_and_res = line.split('"')[1]
            type = type_and_res.split()[0]
            res = type_and_res.split()[1]
            yield (addr, type, res)

if __name__ == '__main__':
    parsed = logs_parse(SERVERFILE)
    for el in parsed:
        print(el)







