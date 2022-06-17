'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...

'''
def odd_num(num):
    for i in range(1, num, 2):
        yield i

gen_odd_num = odd_num(7)
print(next(gen_odd_num))
print(next(gen_odd_num))
print(next(gen_odd_num))


'''
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''

gen_out_yield = (i for i in range(1,34,2))
for i in gen_out_yield:
    print(i)
