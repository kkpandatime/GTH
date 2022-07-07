'''
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker:
    INCOME = {'doctor': {'wage': 22222, 'bonus': 333333}}

    def __init__(employee, name, surname, position):
        employee.name = name
        employee.surname = surname
        employee.position = position
        employee.income = employee.INCOME[position]

    def get_info(employee):
        return f'Name: {employee.name}\nSurname: {employee.surname}\nPosition: {employee.position}'


class Position(Worker):
    def full_name(employee):
        return f'{employee.name} {employee.surname}'

    def total_income(employee):
        return f'{employee.income["wage"] + employee.income["bonus"]}'


worker = Position('Greg', 'House', 'doctor')
print(worker.full_name())
print(worker.total_income())
print(worker.get_info())