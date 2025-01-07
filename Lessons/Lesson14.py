# Modules

import math

print(math.pi)



# Packets

import math

print(dir(math))
print(help(math))



# Classification

import sys

print(sys.builtin_module_names)
print(sys.path, '\n')



# Atribute

print(math.__name__)
print(math.__doc__)
# print(math.__file__)



# Cesh import

from importlib import reload

reload(math)

y = math.gcd(5 * 5)
print(f"y = {y} \n")



from math import (
    pi as PI,
    tan,
    sqrt
)

from math import pi as PI, \
    tan, \
    sqrt



# Overstretch of operations

print("It's " + "Johny!")

print("It's ".__add__("Marry!"))
# print("It's ".__iadd__("Marry!"))


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box [x = {self.x}, y = {self.y}, z = {self.z}]"

box_1 = Box(1, 2, 3)
box_2 = Box(4, 5, 6)

# box_3 = box_1 + box_2
# print(box_3) - Not work!


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box [x = {self.x}, y = {self.y}, z = {self.z}]"

    def __iadd__(self, other):
        print("iadd")
        return Box(self.x + other.x, self.y + other.y, self.z + other.z)

    def __add__(self, other):
        print("add")
        return Box(self.x + other.x, self.y + other.y, self.z + other.z)

box_1 = Box(1, 2, 3)
box_2 = Box(4, 5, 6)

box_3 = box_1 + box_2
print(box_3)

box_3 += box_3
print(box_3, "\n")

# box_3 += 1
# print(box_3)


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box [x = {self.x}, y = {self.y}, z = {self.z}]"

    def __iadd__(self, other):
        if isinstance(other, Box):
            print("iadd")
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __add__(self, other):
        print(type(other))
        if isinstance(other, Box):
            print("add")
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

box_3 = box_1 + box_2
print(box_3)

box_3 += box_3
print(box_3, '\n')

# box_3 += 1
# print(box_3)



class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)

    def __iadd__(self, other):
        # if isinstance(other, Box):
        #     print("iadd")
        #     return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        # return NotImplemented
        return Box.__add__(self, other)

    def __add__(self, other):
        # print(type(other))
        if isinstance(other, Box):
            print("add")
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Box(self.x + other, self.y + other, self.z + other)
        return NotImplemented

box_3 = box_1 + box_2
print(box_3)

box_3 += box_3
print(box_3)

box_3 += 3
print(f"+3: {box_3}")

# box_r = 10 + box_3
# print(box_r)

import numbers
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)

    def __iadd__(self, other):
        # if isinstance(other, Box):
        #     print("iadd")
        #     return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        # return NotImplemented
        return Box.__add__(self, other)

    def __radd__(self, other):
        print("radd")
        return Box.__add__(self, other)

    def __add__(self, other):
        # print(type(other))
        if isinstance(other, Box):
            # print("add")
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, numbers.Real):
            return Box(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Box(self.x * other, self.y * other, self.z * other)
        return NotImplemented

box_3 = box_1 + box_2
print(box_3)

box_3 += box_3
print(box_3)

box_3 += 3
print(f"+3: {box_3}")

box_r = 10 + box_3
print(box_r, '\n')

box_r = box_r + 10 + 6
print(hash(box_r))

box_mul = box_r * 22
print(box_mul, '\n')



# Comparison operator overload

box_1 = Box(1, 2, 3)
box_2 = Box(1, 2, 3)
print(box_1 == box_2)

box = box_1
print(box == box_1)

print(id(box_1))
print(id(box_2))
print(id(box), "\n")



class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)

    def __iadd__(self, other):
        # if isinstance(other, Box):
        #     print("iadd")
        #     return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        # return NotImplemented
        return Box.__add__(self, other)

    def __radd__(self, other):
        print("radd")
        return Box.__add__(self, other)

    def __add__(self, other):
        # print(type(other))
        if isinstance(other, Box):
            # print("add")
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, numbers.Real):
            return Box(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Box(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def volume(self):
        return self.x * self.y * self.z

    def __eq__(self, other):
        if isinstance(other, Box):
            return self.volume() == other.volume()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Box):
            return self.volume() > other.volume()
        return NotImplemented

    def __lt__(self, other):
        # if isinstance(other, Box):
        #     return self.volume(self) < self.volume(other)
        # return NotImplemented
        return not self > other

    def __ge__(self, other):
        return any((self < other, self == other))

    def __le__(self, other):
        return any((self > other, self == other))

    def __ne__(self, other):
        return not self == other

box_1 = Box(1, 2, 3)
box_2 = Box(3, 4, 5)
print(box_1 >= box_2)

box_3 = box_1 + box_2
print(box_3 >= box_2)
print(box_1 <= box_2)
print(box_2 < box_3, '\n')



# Class field management. Descriptors

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {} ]"
        return msg.format(self.name, self.age, self.color)

cat = Cat("Lucius", 22, "Black")
print(cat)
print(cat.color)

cat.color = "Black & White"
print(cat.color, '\n')


class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self._age = age
        self.__color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {} ]"
        return msg.format(self.name, self._age, self.__color)

    def get_color(self):
        return self.__color

cat = Cat("Lucius", 22, "Black")
print(cat)
print(cat._age)

cat._age = 26
print(cat._age)

# print(cat.__color)
print(cat.get_color(), "\n")

print(cat._Cat__color)

cat._Cat__color = "Black & White"
print(cat._Cat__color)
print(cat._age)
cat._age = 22
print(cat._age)
print(cat, "\n")



# How fields are stored in the object

from sys import getsizeof

dct = {"name": "Lucius", "age": 22, "color": "Black"}
tpl = ("Lucius", 22, "Black")
print(getsizeof(dct))
print(getsizeof(tpl))

dct = {"name": "Lucius", "age": 22, "color": "Black", "type": "Meincoun"}
print(getsizeof(dct), "\n")


class Cat:

    def __init__(self, name, age, color):
        self.age = age
        self.name = name
        self.color = color

    # def get_voice_c(self):
    #     res = ""
    #     res = super().get_voice()
    #
    #     print(f"{res} says 'Meow!'")

    def __str__(self):
        return f"Cat: name = {self.name}, age = {self.age}, color = {self.color}"

cat = Cat("Asche", 22, "Dark Black")
print(cat.__dict__)
print(getsizeof(cat))

cat.type = "Wild cat"
print(cat.type)
print(getsizeof(cat))
print(cat.__dict__, '\n')


class Cat:
    __slots__ = ("name", "age", "color")

    def __init__(self, name, age, color):
        self.age = age
        self.name = name
        self.color = color

    def __str__(self):
        return f"Cat: name = {self.name}, age = {self.age}, color = {self.color}"

cat = Cat("Asche", 22, "Dark Black")
print(cat.__slots__)
print(getsizeof(cat), "\n")

# cat.type = "Meincoun"
# print(cat.type)



# Methods

# __getattr__

class Cat:
    __slots__ = ("name", "age", "color")

    def __init__(self, name, age, color):
        self.age = age
        self.name = name
        self.color = color

    def __str__(self):
        return f"Cat: name = {self.name}, age = {self.age}, color = {self.color}"

    def __getattr__(self, atr_name):
        print(atr_name)
        return None

cat = Cat("Asche", 22, "Dark Black")
print(cat.typ)
print(cat.name)
print(cat.abracadabra, "\n")

print(getattr(cat, "name"))
print(getattr(cat, "type"), "\n")


import math

PI = getattr(math, "pi")
print(PI)

pow_math = getattr(math, "pow")
print(pow_math(3, 5), "\n")


fields = ["age", "name", "color", "No type"]
for field in fields:
    print(getattr(cat, field, None))

print("\n", hasattr(math, "pipidaster"))
print(hasattr(math, "pow"), "\n")



# __getattribute__

# No

class Foo(object):
    def __init__(self, a):
        self.a = a

    def __getattribute__(self, attr):
        try:
            return self.__dict__[attr]
        except KeyError:
            return "Default"

# Yes

class Cat:
    def __init__(self, name, age, color):
        self.age = age
        self.name = name
        self.color = color

    def __str__(self):
        return f"Cat: name = {self.name}, age = {self.age}, color = {self.color}"

    def __getattribute__(self, atr_name):
        try:
            return object.__getattribute__(self, atr_name)
        except AttributeError:
            if atr_name == "type":
                return "Wild cat"
            print(atr_name)
            return None

cat = Cat("Lucius", 22, "Black")
print(cat.type)
print(cat.name)
print(cat.object, "\n")


class Cat:
    def __init__(self, name, age, color):
        self.age = age
        self.name = name
        self.color = color

    def __str__(self):
        return f"Cat: name = {self.name}, age = {self.age}, color = {self.color}"

    def __getattr__(self, atr_name):
        if atr_name == "type":
            return "Wild cat"
        return None

    def __getattribute__(self, atr_name):
        # try:
        #     return object.__getattribute__(self, atr_name)
        # except AttributeError:
        #     if atr_name == "type":
        #         return "Wild cat"
        #     print(atr_name)
        #     return None
        return object.__getattribute__(self, atr_name)

cat = Cat("Lucius", 22, "Black")
print(cat.type)
print(cat.name)
print(cat.object, "\n")



# __setattr__

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {} ]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        if atr_name == "type":
            return "Wild cat"
        print(atr_name)
        return "11"

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        print("self field -> ", attr_name)
        self.__dict__[attr_name] = attr_value

cat = Cat("Lucius", 22, "Black")
cat.type = "Devil"
print(cat.type)

cat.color = "Black & White"
print(cat, "\n")


import math

setattr(math, "piiiiiiiiiiiiiii", 22)
cat.name = "Volt"

dct = {"name": "Lucifer", "age": 34}
for key in dct:
    print(getattr(cat, key))

for key, val in dct.items():
    setattr(cat, key, val)

print(cat, "\n")


class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {} ]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        if atr_name == "type":
            return "Wild cat"
        print(atr_name)
        return "11"

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        print("self field -> ", attr_name)
        self.__dict__[attr_name] = attr_value

    def __delattr__(self, attr_name):
        print("remove_field -> ", attr_name)
        del self.__dict__[attr_name]

cat = Cat("Lucius", 22, "Black")
cat.type = "Wild cat"
print(cat)
del cat.type
print(cat, "\n")




