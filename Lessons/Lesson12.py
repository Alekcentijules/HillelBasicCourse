# Classes

class Car:
    color = "Black"
    engine = 2.0
    brand = "Ford"

print(Car.color)
print(type(Car))
print(type(object))
print(type(''), '\n')

c1 = Car()
print(c1)
print(c1.color, '\n')

c1.color = "White"
print(c1.color)
print(c1.engine)
print(c1.brand, '\n')

print(Car.color, '\n')


print(''.istitle())
print(''.istitle, '\n')


class Ford(Car):
    pass

print(Ford.brand)
print(Ford.color, '\n')


# __init__

class Cat:
    ration = 'Borshch'
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

cat = Cat("Varsik", 6, "Black")

print(cat)

cat2 = Cat("Mars", 3, "White")
print(cat2.age)
print(cat2.color, '\n')

cat2.owner = "Meow"
print(cat2.owner, '\n')

# print(cat.owner)

print(Cat.ration, '\n')


class Cat:
    # def __new__(cls, *args, **kwargs):
    #     print("Creating Cat instance")
    #     self = super().__new__(cls)
    #     print(self)
    #     return self

    def __init__(self, name, age, color):
        print("Cat instance fields")
        self.name = name
        self.age = age
        self.color = color

    def meow(self):
        return "Meow meow"

    def __str__(self):
        return f"Cat: name = {self.name}, age = {self.age}, color = {self.color} {self.meow()}"

bars = Cat("Bars", 2, "Yellow")
print(bars)

print(bars.__str__())

print(["MEOOOOOOWWWW!!!!"].__str__(), '\n')


class KillerPhone:
    def __init__(self, target, name, age, price):
        self.target = target
        self.name = name
        self.age = age
        self.price = price

    def __str__(self):
        return f"Kill {self.target}, name = {self.name}, age = {self.age}, price = {self.price}$"

killer_phone_target1 = KillerPhone("Man", "Jango...", 47, 1000000)
print(killer_phone_target1)

print(hash(killer_phone_target1), '\n')


class Warehouse:
    def __init__(self, address):
        self.address = address
        self.storage = {}

    def add_to_storage(self, item, value):
        self.storage[item] = value

    def remove_from_storage(self, item):
        value = self.storage.pop(item, None)

    def get_item_value(self, item):
        return self.storage.get(item, 0)

    def get_total_value(self):
        total = 0
        for key, cnt in self.storage.items():
            total += key.price * cnt
            return total

    def __str__(self):
        tmp = ''
        for item, cnt in self.storage.items():
            tmp += f"{str(item)}: {cnt} pcs. \n{tmp}"
        return f"Warehouse at {self.address} contains: \n{tmp}"

wh = Warehouse("Los Santos, st. Erixonix, 34")
print(wh.get_total_value())

wh.add_to_storage(killer_phone_target1, 54)
print(wh.get_total_value(), '\n')
# print(wh.get_item_value())


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Laptop {self.brand} {self.model} {self.price}$"

notebook1 = Laptop("BlackDevil", "DevilBook 666", 666666)
notebook2 = Laptop("Ninja", "Katana 3000", 333333)
wh.add_to_storage(notebook1, 145)
wh.add_to_storage(notebook2, 267)
print(wh.get_total_value())
print(wh, '\n')


class LightSwitch():
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def switch(self):
        self.switch_is_on = not self.switch_is_on
    def show(self):
        return self.switch_is_on

switch = LightSwitch()
print(switch.show())

switch.turn_on()
print(switch.show())

switch.turn_off()
print(switch.show())

switch.switch()
print(switch.show(), '\n')


switch1 = LightSwitch()
switch2 = LightSwitch()
switch3 = LightSwitch()
switch4 = LightSwitch()
switch5 = LightSwitch()
print(switch3.show())

switch3.turn_on()
print(switch3.show(), '\n')



# @staticmethod

class Cat:
    name = "Mars"

    def __init__(self, name, age, color):
        print("Cat instance fields")
        self.name = name
        self.age = age
        self.color = color

    def meow(self, tmp):
        print(f"Meow meow {tmp}")
        self.say_hello(self.name)

    def __str__(self):
        return f"Cat: name = {self.name}, age = {self.age}, color = {self.color}"

    @staticmethod
    def say_hello(name):
        print(f"Hello {name}")

bars = Cat("Bars", 2, "Yellow")
print(bars)

print(Cat.name)
print(bars.name, '\n')
bars.say_hello("Lucius")

bars.meow("Baby!")
print("\n")



# @classmethod

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box [x = {self.x}, y = {self.y}, z = {self.z}]"

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def up():
        print("up")

    @classmethod
    def print_class_info(cls):
        print(str(cls))

box_1 = Box(1, 2, 3)
box_1.print_class_info()
Box.print_class_info()
print('\n')


from datetime import date

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18

person1 = Person("Mandan", 22)
person2 = Person.from_birth_year("Mandan", 1999)
person3 = person2.from_birth_year("Mandan", 3000)

print(person1.age)
print(person2.age)
print(person3.age, '\n')


class MyClass:

    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS += 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)

my_ob1 = MyClass()
my_ob2 = MyClass()
my_ob3 = MyClass()
my_ob4 = MyClass()

MyClass.total_objects()

my_ob1.TOTAL_OBJECTS
MyClass.TOTAL_OBJECTS
print('\n')



class Car:

    def __init__(self, color, engine, brand, name):
        self.color = color
        self.engine = engine
        self.brand = brand
        self.name = name

    def __str__(self):
        return f"{self.brand} {self.name}"

car1 = Car('Red', 2.8, "Ford", "Mustang")
car2 = Car("Black", 3.0, "Porsche", "911")
car3 = Car("Black", 5.6, "Mercedes", "Rangen")

class Garage:

    def __init__(self, owner):
        self.owner = owner
        self.car_set = set()

    def add_car(self, car):
        self.car_set.add(car)

    def __str__(self):
        if not self.car_set:
            return "Garage is empty...."
        tmp = ""
        for car in self.car_set:
            tmp += f"{str(car)}\n"

        return tmp

garage = Garage("Bob Murley")
print(garage)

garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)
print(garage)

