'''
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors,
необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''


def gen_of_pairs(tutors, klasses):
    for i in range(max(len(tutors), len(klasses))):
        if i < len(tutors) and i < len(klasses):
            pair = (tutors[i], klasses[i])
        elif len(klasses) < len(tutors):
            pair = (tutors[i], None)
        else:
            break
        yield pair
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В',
           '8Б', '10А', '10Б', '9А']

print(type(gen_of_pairs(tutors, klasses)))

for i in gen_of_pairs(tutors, klasses):
    print(i)
