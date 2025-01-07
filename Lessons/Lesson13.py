# Inharitance

class Animal:

    def __init__(self, age, ration, color):
        self.age = age
        self.ration = ration
        self.color = color

    def get_voice(self):
        return Animal

    def __str__(self):
        return f"age = {self.age}, ration = {self.ration}, color = {self.color}"

class Cat(Animal):

    def __init__(self, age, ration, color, name, cat_type):
        super().__init__(age, ration, color)
        self.name = name
        self.cat_type = cat_type

    def get_voice_c(self):
        res = ""
        res = super().get_voice()

        print(f"{res} says 'Meow!'")

    def __str__(self):
        return f"Cat: {super().__str__()}, name = {self.name}, cat_type = {self.cat_type}"

barsik = Cat(5, 'Meat', 'Black', 'Back', 'Meinkun')
print(barsik)
barsik.get_voice_c()
print("\n")


class Dog(Animal):

    def __init__(self, age, ration, color, name, dog_type):
        super().__init__(age, ration, color)
        self.name = name
        self.dog_type = dog_type

    def get_voice_d(self):
        res = ""
        res = super().get_voice()

        print(f"{res} says 'Woof!'")


rex = Dog(3, "Meat", "Black", "Rex", "Doberman")
print(rex)
rex.get_voice_d()

print("\n", rex.dog_type)
print(str(rex))
print(rex.name, "\n")


animal_ = Animal(4, "Fish", "Black and White")
print(animal_, "\n")



# Abstraction

from abc import ABC, abstractmethod
class Animal(ABC):

    def __init__(self, age, ration, color):
        self.age = age
        self.ration = ration
        self.color = color

    # @abstractmethod
    # def get_voice(self):
    #     pass

    def __str__(self):
        return f"age = {self.age}, ration = {self.ration}, color = {self.color}"

animal = Animal(6, "kabel", "Black and White")

print(issubclass(Dog, Animal), issubclass(Animal, Dog), '\n')
print(isinstance(rex, Dog))

print("cat", str)
print(type("cat") == str)
print(isinstance(2.2, (int, float)))
print(isinstance("22", (int, float, str)), "\n")


# class Base:
#
#     def price(self):
#         return 10
#
# class Discount(Base):
#
#     def price(self):
#         return self.price() * 0.8
#
# d = Discount()
# print(d.price()) - Not work!


# Variant 1
class Base:

    def price(self):
        return 10

class Discount(Base):

    def price(self):
        return Base.price(self) * 0.8

d = Discount()
print(d.price())


# Variant 2

class Base:

    def price(self):
        return 10

class InterFool(Base):

    def price(self):
        return super().price() * 1.1

class Discount(InterFool):

    def price(self):
        # return super(Discount, self) * 0.8
        return super().price() * 0.8

d = Discount()
print(d.price(), '\n')


class A:

    def __init__(self):
        self.x = 22

class B(A):

    def __init__(self):
        super().__init__()
        self.y = round(self.x * 10.1)

b = B()
print(b.y)

print(super(InterFool, d).price())
print(super(Discount, d).price(), "\n")



class A:
    def print_smile(self):
        print(":)")

class B(A):
    def print_sad_smile(self):
        print(":(")

class C(A):
    def print_both_smile(self):
        print(":( :)")

class D(B):
    def print_sad_smile(self):
        print("^)")

example = D()
example.print_smile()
# print(example.print_both_smile())
example.print_sad_smile()

print("\n", D.mro())
print(C.mro())
print(A.mro())
print(D.__mro__)
print(example.__hash__(), '\n')


class A:
    def print_smile(self):
        print(":)")

class B:
    def print_smile(self):
        print(":0")

class C(B, A):
    pass

my_var = C()
my_var.print_smile()
print(C.mro(), '\n')



class D:
    def print_smile(self):
        print("(-_-)")

class A(D):
    pass

class B:
    def print_smile(self):
        print(";P")

class C(A, B):
    pass

my_var = C()
my_var.print_smile()
print(C.mro(), '\n')


class Animal:
    def __init__(self, age, ration, color):
        self.age = age
        self.ration = ration
        self.color = color

    def get_voice(self):
        print("Animal")

    def __str__(self):
        return f"age = {self.age}, ration = {self.ration}, color = {self.color}"

class Cat(Animal):
    def __init__(self, age, ration, color, name, cat_type):
        super().__init__(age, ration, color)
        self.name = name
        self.cat_type = cat_type

    def get_voice(self):
        print("Meow!")

    def __str__(self):
        return f"Cat: {super().__str__()}, name = {self.name}, cat_type = {self.cat_type}"

    def __repr__(self):
        result = super().__repr__()
        return f"Bonjour! {result}"

cat = Cat(22, "Meat", "Black", "Lucius", "Meincoun")
cat.get_voice()
print(Cat.mro())
print(repr(cat), "\n")


class Engine:
    def __init__(self, fuel, volume, turbo=False):
        self.fuel = fuel
        self.volume = volume
        self.turbo = turbo

    def __str__(self):
        return f"{self.volume}::{self.fuel}"

class Driver:
    def __init__(self, name, last_name, number, birthday):
        self.name = name
        self.last_name = last_name
        self.number = number
        self.birthday = birthday

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Car:
    def __init__(self, color, model, year, some_engine):
        self.color = color
        self.model = model
        self.year = year
        self.some_engine = some_engine
        self.driver = None
        self.number = None

    def add_driver(self, some_driver):
        self.driver = some_driver

    def add_number(self, number):
        if not self.driver:
            return "No!"
        else:
            self.number = number
            return "Added"
    def get_driver_info(self):
        if not self.driver:
            return "No driver!"
        return str(self.driver)

    def __str__(self):
        return f"{self.model}:{self.number} :{self.some_engine.volume}\n {self.get_driver_info()}"

engine = Engine("Disel", 2.2, True)
print(engine)
print(engine.volume)

driver = Driver("Alexcent", "Ijules", "122/679-13", "22-05-2005")
print(driver, "\n")

corboba = Car("Red", "Corboba", 2222, engine)
print(corboba)

print(corboba.add_number("AAA949343AU"))

corboba.add_driver(driver)
print(corboba.add_number("AAA949343AU"))

print(corboba, '\n')



class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12

class Employee:
    def __init__(self, name, pay, bonus):
        self.name = name
        self.salary = Salary(pay)
        self.bonus = bonus

    def get_salary(self):
        return f"{self.salary.get_total() + self.bonus}$"

employee = Employee("Strage Samik", 2222, 1300)
print(employee.get_salary())

s = Salary(654)
print(s.get_total())



# Exceptions

# index = int(input("Enter index: "))
# my_list = [0, 1, 3, 7]
#
# try:
#     print(my_list[index])
#
# except IndexError:
#     print("You enter wrong index!")
# print("OK")
#
#
# try:
#     print(my_list[index])
#
# except Exception:
#     print("You enter wrong index!")
# print("OK")



# index = int(input("Enter index: "))
# my_list = [0, 1, 3, 7]

# try:
#     t = my_list[index]
#     print(t)
#     t += 22
#     print("Oki-doki")
# except IndexError:
#     print("You enter wrong index!")
#
# f = 6 + t
# print(f)


# t = 0
#
# try:
#     t = my_list[index]
# except IndexError:
#     print("You enter wrong index!")
#
# print(t)
# t += 22
# print("OKI-DOKI")
# f = 2 + t
# print(f)


def sub100(index):
    my_list = [0, 6, 8]
    return 100 / my_list[index]

# index = int(input("Enter index: "))
#
# try:
#     print(sub100(index))
# except IndexError:
#     print("You enter wrong index!")
# except ZeroDivisionError:
#     print("Error: division by zero!")


index = 22
try:
    print(sub100(index))
except IndexError as err:
    print(type(err))
    print(err)



# index = int(input("Enter index: "))
#
# try:
#     res = sub100(index)
# except IndexError:
#     print("You enter wrong index!")
# except ZeroDivisionError:
#     print("Error: division by zero!")
# else:
#     print(res)


# index = int(input("Enter index: "))
# res = None

# try:
#     res = sub100(index)
# finally:
#     print("-" * 10, res)

# try:
#     res = sub100(index)
# except IndexError:
#     print("You enter wrong index!")
# except ArithmeticError:
#     print("Error: division by zero!")
# else:
#     print(res)
# finally:
#     print("-" * 10, res)


text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# with open("zen.txt", "w+") as file:
#     file.write(text)
#
# import time
#
# try:
#     file = open("zen.txt")
#     while True:
#         line = file.readline()
#         if len(line) == 0:
#             break
#         print(line, end="")
#         time.sleep(2)
# except KeyboardInterrupt:
#     print("You close read file!")
# finally:
#     file.close()
#     print("Cleaning: Canceling file")


print('\n', issubclass(ArithmeticError, Exception))
print(issubclass(ZeroDivisionError, BaseException))

print(IndexError.mro())
print(ZeroDivisionError.mro(), '\n')


def magic_func(x):
    if x == 1:
        raise ValueError("This is trouble! x = 1!!!!!!!!!!!!!!!")
    else:
        return [x]

y = 1 #int(input("Type some integer: "))

try:
    lst = magic_func(y)
except ValueError as e:
    print(str(e))
except Exception as e:
    print(str(e))
else:
    print(lst)



class UserException(Exception):
    def __init__(self, message, x):
        super().__init__()
        self.message = message
        self.x = x

    def get_exeption_message(self):
        return self.message

number = int(input("Enter a positive number!: "))

def positive(num):
    if num < 0:
        raise UserException("Negative number value!: ", num)
    return num

try:
    a = positive(number)
except UserException as err:
    print(err.get_exeption_message())
    print(err.x)
    # print(err.message)
# print(number)



# assert

# assert 2 == 22

# if not 2 == 22:
#     raise AssertionError("Some error!")

print("\n", AssertionError.mro())

assert 3 == 3, "Not some error!"


# def easy_unpack(elements: tuple) -> tuple:
#     return elements[0], elements[2], elements[-2]
#
# assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9) == (1, 3, 7))
# assert easy_unpack((1, 1, 1, 1) == (1, 1, 1))
# assert easy_unpack((6, 3, 7) == (6, 7, 3))
# print("OKI-DOKI")
