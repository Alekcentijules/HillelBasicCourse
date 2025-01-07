# __name__ and __module

from math import pow
print(pow.__module__, "\n")



# dir
def sum(a, b: list) -> int:
    """
    This function +
    :param a:
    :param b:
    :return: a + b
    """

    return a + b

print(sum(2, 4))
print(dir(sum), '\n')



# __code__

print(sum.__code__, '\n')



# __doc__

print(sum.__doc__, '\n')
help(sum)
print(str.__doc__)
print(str.find.__doc__, '\n')



# lambda

g = lambda x: x ** 2

print(g(6))


q = lambda x, y: x ** 2 + y if y <= 5 else x ** 3 + y

print(q(6, 3), '\n')



# map()

num_lst = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 5, num_lst))

print(squared, '\n')



# pow()

# print(pow(2, 3, 3))



# filter()

print(list(filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])), '\n')



# zip()

print(list(filter(None, zip(["One", "Two", "Three"], [0, 2, 3, 4]))), '\n')



# Generators

gen = range(5)

print(gen)

# num_lst = [1, 2, 3, 4]
gen_exp = (x ** 2 for x in range(3))

print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp), '\n')
# print(next(gen_exp))
# print(next(gen_exp), '\n')


def fibonacci(num):
    a, b = 0, 1

    for i in range(num):
        yield a

        a, b = b, a + b


# for i in fibonacci(14):
#     print(i)

fib = fibonacci(5)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib), '\n')
# print(next(fib))



# send()

def s_gen():
    print("Start")
    x = yield 69
    print(f'Received: {x}')

new_gen = s_gen()
print(next(new_gen), '\n')
# print(new_gen.send(99))
# print(new_gen.send(None))



# getgeneratorstate()

from inspect import getgeneratorstate

gen = s_gen()

print(getgeneratorstate(gen))



# Recursies

def count_num(s):
    # if len(n) == 1 or 2:
    #     if n[0] == n[-1]:
    #         return True
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return count_num(s[1:-1])

print(count_num("aba"))


def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)

print(fact(5))



def summ(lst):
    if len(lst) == 0:
        return 0

    return lst[0] + summ(lst[1:])

lsti = [1, 2, 3]
print(summ(lsti))


def summ2(a, b):
    if a == b:
        return a

    return b + summ2(a, b -1)


print(summ2(2, 5))

