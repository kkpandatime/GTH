'''
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия
одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''

def checkup(measures):
    while True:
        value = input(f'{measures}')
        try:
            value = float(value)
            break
        except ValueError:
            print('Incorrect value')
    return value


class Road:
    def __init__(estimate, length: float, width: float):
        estimate.length = length
        estimate.width = width
        estimate.weight = 100

    def total_weight(estimate, thickness: float):
        total_weight = estimate.length * estimate.width * estimate.weight * thickness
        print(f'Asphalt mass for a {estimate.width * estimate.length} sq.m. road - {total_weight} kg.')


if __name__ == '__main__':
    length_of_road = checkup('Lenght (m): ')
    width_of_road = checkup('Width (m): ')
    total_road = Road(length_of_road, width_of_road)
    layer_thickness = checkup('Thickness(сm): ')
    total_road.total_weight(layer_thickness)