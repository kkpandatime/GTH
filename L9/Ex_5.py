'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(art, title: str):
        art.title = title

    def draw(art):
        print(f'Start drawing {art.title}')


class Pen(Stationery):
    def __init__(art, title):
        super().__init__(title)

    def draw(art):
        print(f'Bitmap drawing {art.title}')


class Pencil(Stationery):
    def __init__(art, title):
        super().__init__(title)

    def draw(art):
        print(f'Hatching {art.title}')


class Handle(Stationery):
    def __init__(art, title):
        super().__init__(title)

    def draw(art):
        print(f'Paint over {art.title}')


paintbrush = Stationery('Paintbrush')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

paintbrush.draw()
pen.draw()
pencil.draw()
handle.draw()