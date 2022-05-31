'''
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию,
написав минимум кода?
'''

initial_prices = [100.81, 12.3, 56.25, 79.13, 61.2, 5.0, 222.33,
              944.0, 456.12, 32.1, 78.94, 85.2, 63.4, 1234.68]

def format_prices(initial_prices):
    formated_prices = []
    for price in initial_prices:
        formated_prices.append(f'{int(price)} руб {int((price - int(price)) * 100):02d} коп')
    return formated_prices

print('All prices:', initial_prices)
print('Formated:', format_prices(initial_prices))
print('ID:', id(initial_prices))
initial_prices.sort()
print('ID sorted:', id(initial_prices))
print('Formated and sorted:', format_prices(initial_prices))
sorted_reversed = sorted(initial_prices, reverse=True)
print('Formated and sorted reversed:', format_prices(sorted_reversed))
print('Top 5:', format_prices(sorted_reversed[:5]))
