'''
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

import time

class TrafficLight:
    def __init__(lights):
        print(f'--Traffic light on--')
        lights.color = ('RED', 'YELLOW', 'GREEN')
        lights.mode = 0
        lights.duration = (7, 2, 10)

    def running(lights):
        print(f'The {lights.color[0]} light is on!')

    def stop(lights):
        lights.mode = 0
        print(f'Traffic light off')

    def switch(lights):
        if lights.mode != 2:
            lights.mode += 1
        else:
            lights.mode = 0
        print(f'Traffic light switch to {lights.color[lights.mode]}')

    def switch_auto(lights, arg=3):
        for el in range(arg):
            time_light = lights.duration[lights.mode]
            dur_of_time = time_light
            while dur_of_time > 0:
                print(f'{lights.color[lights.mode]}. {dur_of_time} sec left.')
                dur_of_time = dur_of_time - 1
                time.sleep(1)
            lights.switch()
        print(f'Traffic light stopped, {lights.color[lights.mode]} light on now.')


if __name__ == '__main__':
    new_trafficlight = TrafficLight()
    new_trafficlight.running()
    quit = False
    while not quit:
        user_control = input('1 - Manual switching\n'
                             '2 - Auto switching\n'
                             '3 - Exit\n'
                             'Select an action: ')
        if user_control == '3':
            new_trafficlight.stop()
            break
        if len(user_control) == 1:
            try:
                mode = int(user_control)
                if mode == 1:
                    new_trafficlight.switch()
                elif mode == 2:
                    new_trafficlight.switch_auto()
            except ValueError:
                pass

    print('Exit')