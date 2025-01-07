# Generators

g_lst = (i ** 2 for i in range(10000))

print(g_lst, '\n')


for i in g_lst:
    print(i, end=" ")
    if i == 36:
        break

for i in g_lst:
    print(i, end=" ")
    if i == 100:
        break

print(next(g_lst), '\n')



# gen_lst

a = [1, 3, 5, 7]

b = [[x * y for x in a] for y in range(4)]

print(b)


d = {i: v for i, v in enumerate(b)}

print(d, '\n')


import time

start = time.time()
c = (i ** 2 for i in range(10_000_000))
end = time.time()
print("for generator t = ", end-start, " s", '\n')



# Contribution functions

def calculate_pow(n):
    def calculate(num):
        print(locals())
        return num ** n

    return calculate

f = calculate_pow(5)

print(f(3))



def fibonacci():
    f_num = 0
    s_num = 1
    def get_next():
        nonlocal f_num
        nonlocal s_num
        next_num = s_num + f_num
        f_num = s_num
        s_num = next_num
        return next_num
    return get_next

f = fibonacci()

for i in range(12):
    print(f(), end="-")
print('\n')


# Decorators

my_func = []

def add_func(func):
    my_func.append(func)

    return func

@add_func
def summ(x, y):
    return sum(x, y)

@add_func
def mul(x, y):
    return x * y

print(my_func)
print(mul(2, 4))


def div(x, y):
    return x / y

print(div(5, 6))

div = add_func(div)

print(my_func, '\n')



import functools
def to_str(func):
    """I do string!"""
    @functools.wraps(func)
    def get_str(*args, **kwargs):
        """I do str!"""
        return str(func(*args, **kwargs))
    # get_str.__module__ = func.__module__
    # get_str.__doc__ = func.__doc__
    # get_str.__name__ = func.__name__

    # functools.update_wrapper(get_str, func)

    return get_str

@to_str
def suma(x, y):
    """I do summ!"""
    return x + y

print("Summa = " + suma(2, 23), '\n')

print(suma.__name__, suma.__doc__, suma.__module__, '\n')



def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#SeniorroPomidorro")
        func()
        print("~Salatssss~")
    return wrapper

def sandwich(food="==Bifshtacs=="):
    print(food)


sandwich()

sandwich = bread(ingredients(ingredients(sandwich)))
sandwich()
print('\n')



a = 1
def decorator_with_args(deco_arg1, deco_arg2):
    print("Dec. with args: ", deco_arg1, deco_arg2)
    def my_lovely_dec(func):
        print("My lovely dec. Args without: ", deco_arg1, deco_arg2)
        def wrapper(func_arg1, func_arg2):
            print("""Here all arguments without: \n {0} {1}\n" 
            {2} {3}""".format(deco_arg1, deco_arg2, func_arg1, func_arg2))
            return func(func_arg1, func_arg2)
        return wrapper
    return my_lovely_dec

b = 2

@decorator_with_args("Booba", "Woowa")
def decorated_function_with_args(_arg1, _arg2):
    print("Decorated function is know self arguments: {0} {1}".format(_arg1, _arg2))

print("----------------STAAAAART!!!!!----------------")
decorated_function_with_args("Aladdin with him", "Flying carpet")
print('\n')


beautiful_workers = {}

def link(adress=None):
    def add_worker(func):
        beautiful_workers[adress] = func
        def get_answer(*args, **kwargs):
            return str(func(*args, **kwargs))
        return get_answer
    return add_worker

@link("\main")
def main_page():
    return "Hello my beautiful workers!"

@link("\main\goods")
def get_goods(list_goods):
    return list_goods

print(beautiful_workers)

@link()
def black_world():
    return "Hello black world..."

print(beautiful_workers, '\n')



import functools
import time

@functools.lru_cache()
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
result = fibonacci(260)

print(result)
print(time.time() - start, '\n')



def cache(func):
    data = {}
    def wrapper(*args):
        if args in data:
            return data[args]
        else:
            result = func(*args)
            data[args] = result
            return result

    return wrapper

@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
res = fibonacci(260)

print(res)
print(time.time() - start)




