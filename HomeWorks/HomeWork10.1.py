def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    for i in range(end):
        yield begin
        begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, lambda x: x ** 2)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')


next_gen = some_gen(2, 7, lambda x: x ** 2)

for i in range(7):
    print(next(next_gen))









