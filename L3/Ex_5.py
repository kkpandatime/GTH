'''
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
'''

from random import choice
def get_jokes(num_jokes, repeat=False):
    jokes_variations = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(num_jokes):
        if not repeat:
            if num_jokes > len(nouns) or num_jokes > len(adverbs) or num_jokes > len(adjectives):
                print('No more variations')
                return None
            else:
                noun = choice(nouns)
                adverb = choice(adverbs)
                adjective = choice(adjectives)
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)

            joke_result = ' '.join([noun, adverb, adjective])
        else:
            joke_result = ' '.join([choice(nouns), choice(adverbs), choice(adjectives)])
        jokes_variations.append(joke_result)
    return jokes_variations

print(get_jokes(1))
print(get_jokes(2))
print(get_jokes(3))
print(get_jokes(4))