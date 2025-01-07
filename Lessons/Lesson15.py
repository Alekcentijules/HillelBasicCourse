# property

class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        print("Call get name...")
        return self.__name

    def set_name(self, name_value):
        print("Call set name...")
        self.__name = name_value

    def del_name(self):
        print("Call remove name...")
        del self.__name

    name = property(get_name, set_name, del_name, " Cat name")

    def __str__(self):
        msg = "Cat [ name = {}, age = {} ]"
        return msg.format(self.name, self.age)

cat1 = Cat("Bober", 5)

cat1.name = "Lucius"
print(cat1.name)
print(cat1)


class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    name = property()

    @name.getter
    def get_name(self):
        print("Call get name...")
        return self.__name

    @name.setter
    def set_name(self, name_value):
        print("Call set name...")
        self.__name = name_value

    @name.deleter
    def del_name(self):
        print("Call remove name...")
        del self.__name

cat = Cat("Lucius", 22)
# print(cat.name)
# cat.name = "Konstantin"
# print(cat)
# del cat.name
print(cat, "\n")


class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

cat = Cat("Lucius", 22)
print(cat.name, "\n")



# Descriptors

class MyDescriptor:
    def __init__(self, n):
        self.n = n

    def __get__(self, instance_self, instance_class):
        print(self)
        print(instance_self)
        print(instance_class)
        return self.n * instance_self.p

class Box:
    volume = MyDescriptor(2)

    def __init__(self, x, y, z):
        self.p = x * y * z

box1 = Box(1, 2, 5)
print(box1.volume)

box1.volume = 22
print(box1.volume)


class ProtectedField:
    def __init__(self, field):
        self.field = field

    def __get__(self, instance_self, instance_class):
        field = f"_{instance_class.__name__}{self.field}"
        return getattr(instance_self, field)

class Cat:
    name = ProtectedField("__name")
    age = ProtectedField("__age")

    def __init__(self, _name, _age):
        self.__name = _name
        self.__age = _age

cat = Cat("Lucius", 22)
# print(cat.__name)
print(cat._Cat__name)
print(cat.name, "\n")

cat.name = "Voland"
print(cat.name)
print(cat._Cat__name, "\n")


class ProtectedField:
    def __init__(self, field):
        self.field = field

    def __get__(self, instance_self, instance_class):
        field = f"_{instance_class.__name__}{self.field}"
        return getattr(instance_self, field)

    def __set__(self, instance_self, value):
        instance_class = instance_self.__class__
        field = f"_{instance_class.__name__}{self.field}"
        setattr(instance_self, field, value)

class Cat:
    name = ProtectedField("__name")
    age = ProtectedField("__age")

    def __init__(self, _name, _age):
        self.__name = _name
        self.__age = _age

cat = Cat("Bobin", 22)
print(cat.name)
cat.name = "Lucius"
print(cat.name)
print(cat._Cat__name, "\n")


# Iterators and iterator protocol

class UserSequence:
    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        if index < self.number:
            return index ** 2
        else:
            raise IndexError

    def __len__(self):
        return self.number

seq = UserSequence(22)

for i in range(len(seq)):
    print(seq[i])

print(seq[13], "\n")
# print(seq[4:14])



# slice()

slice_ = slice(0, 4, 2)
print(slice_)
print(slice_.start)
print(slice_.stop)
print(slice_.step, "\n")


a = [4, 6, 1, 77, 2, 13, 22]
print(a[slice_])
print(a[0:4], "\n")

print(a[slice(2, None)])
print(a[2:])
print(a[slice(None, -1)])
print(a[:-1])
print(a[slice(None, None, 2)])
print(a[::2])
print(a[slice(None)])
print(a[::])
print(a[slice(3)])
print(a[:3:], "\n")

user = slice(None, None, -1)
print(a[user])
print(a[::-1])

sl = slice(None, None, -1)
print(sl)
print(sl.start)


class UserSequence:
    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start and index.start < 0:
                raise IndexError
            elif index.stop and index.stop > self.number:
                raise IndexError
            result = []
            start = 0 if index.start is None else index.start
            stop = self.number if index.stop is None else index.stop
            reverse = False

            if index.step and index.step < 0:
                reverse = True
                step = index.step * (-1)
            else:
                step = 1 if index.step is None else index.step

            for i in range(start, stop, step):
                result.append(i ** 2)
            return list(reversed(result)) if reverse else result

        if isinstance(index, int):
            if index < self.number:
                return index ** 2
            else:
                raise IndexError
        raise TypeError

    def __len__(self):
        return self.number

seq = UserSequence(22)
print(seq)
print(seq[1:13])
print(seq[:10:-1])
print(seq[:])
print(seq[:10:3], "\n")



# Iterators

str_ = "Hello, Baby!"
it = iter(str_)
print(type(it))
print(it)
print(next(it))
print(next(it))

lst = ["Hello", ",", "Tutsi", "!"]
lst_iter = lst.__iter__()
print(type(lst_iter))

# for i in lst_iter:
#     print(i)

print(lst_iter.__next__())
print(lst_iter.__next__(), "\n")


class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Goods [ name = {self.name}, price = {self.price} ]"

class Basket:
    def __init__(self, user):
        self.user = user
        self.goods_lst = list()

    def add_goods(self, good):
        self.goods_lst.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_lst:
            result += str(good) + "\n"
        return result

basket = Basket("Adolf")
basket_2 = Basket("Voland")
print(basket)

ap = Goods("Fresh apple...", 22)
mk = Goods("Spycy milk", 34)

basket.add_goods(ap)
basket.add_goods(mk)

print(basket, "\n")

# for good in basket:
#     print(good)


class BasketIterator:
    def __init__(self, goods_lst):
        self.goods_lst = goods_lst
        self.index = 0

    def __next__(self):
        if self.index < len(self.goods_lst):
            res = self.goods_lst[self.index]
            self.index = self.index + 1
            return res
        else:
            raise StopIteration

    def __iter__(self):
        return self

class Basket:
    def __init__(self, user):
        self.user = user
        self.goods_lst = list()

    def add_goods(self, good):
        self.goods_lst.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_lst:
            result += str(good) + "\n"
        return result

    def __iter__(self):
        return BasketIterator(self.goods_lst)

basket = Basket("Jango_0-0")

ap = Goods("Fresh apple...", 22)
mk = Goods("Spycy milk", 34)

basket.add_goods(ap)
basket.add_goods(mk)

print(basket)

for good in basket:
    print(good)







