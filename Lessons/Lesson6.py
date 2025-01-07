# eval()
print("eval(): ", eval('134.343 * 4'))

form = '({x} * {y}) / {y}'
r1 = eval(form.format(x=4, y=10))
print(r1)

form2 = '{r}/100'
print(eval(form2.format(x=5, y=100, z=5, r=r1)), "\n")

coord = [3, 6]

print('x: {0[0]}; y: {0[1]}'.format(coord))

print(f'x: {coord[0]}; y: {coord[1]} \n')

print('{:<10}'.format("WOW"))
print('{:>10}'.format("WOW"))
print('{:^10}'.format("WOW"))
print('{:$^10}'.format("WOW"), '\n')

a = "WOWPIK"

print(f'|{a:<10}|')
print(f'|{a:>10}|')
print(f'|{a:^10}|')
print(f'|{a:$^10}| \n')

points = 22.2
total = 44

print('Correct answers: {:.5%}'.format(points/total), '\n')



# exec()
exec('print("OK") \n')
# print('\n')



# bites

# .encode()
text = 'Hello world!'
b_text = text.encode()

print(b_text)
print(type(b_text))

text = 'Привіт, світ!'
b = text.encode('utf-8')

print(b)
print(type(b))
print(len(b), '\n')

# .decode()
s = b.decode("utf-8")

print(s)
print(type(s))
print(len(s), '\n')

print("Windows 1251: ", b.decode("windows-1251"), '\n')



# Cortages

# tuple()
b = tuple()
print("Type tuple: ", type(b))

a = ()
print(type(a))

c = (4, 7, "Abrakadabra!")
print(type(c))

a = (3)
print(type(a))

a = 6,
print(type(a))

a = (6, )
print(type(a))

b, t = 3, 6
print(type(b), type(t), '\n')

b = tuple([5])
print(b)
print(type(b), '\n')

my_tuple = tuple('Hello, world!')
print(my_tuple, '\n')



# sys

import sys

lst = [10, 20, 40]
tpl = tuple(lst)

print(sys.getsizeof(lst))
print(sys.getsizeof(tpl))

l = []
print(sys.getsizeof(l))
t = ()
print(sys.getsizeof(t), '\n')


my_tuple = (1, 2, 4, [3, "Hello"], (5, 6, 7))
print(my_tuple)



# del
# del my_tuple[9] - not work!

lst = ["a", "b"]
my_tuple = (1, 2, lst, 3, 4)
print(my_tuple)

my_tuple[2][1] = "BOOOM, SHAKALAKAAAA"
my_tuple[2][0] = 10000000
print(my_tuple, '\n')

lst.pop()
print(".pop(): ", my_tuple)

del lst

print(my_tuple)

my_tuple[2].append("I'm HEEEEEEEREEEEEE!!!!")
print(my_tuple, '\n')

lst = "Tick-tick-tick-BOOOOOOOOOOMMM!!!!!!"
my_tuple = (1, 2, lst, 3, 4)
print(my_tuple)

lst = "Pick-pick-picl-Booomm!"
print(my_tuple, '\n')



# dict
d1 = dict()
d2 = {}

print(type(d1))
print(type(d2), '\n')

d1 = dict(Ivanushka='Manager', Marchik='Worker')
print(d1)

d2 ={"A1": "123", "A2": "456"}
print(d2)

gender_dict = {0: "Man", 1: "Woman"}
print(gender_dict, '\n')

dct = {1.0: 'One'}
print(dct)

dct[1] = "Hy!"
print(dct)



# hash()
print(hash(10))
print(hash("10"))
print(hash("Hello world!"))
print(hash((1, 3)), '\n')
# print(hash([1, 3])) - not work!

# a = d2[1]
# print(a)

print(d2['A1'])
print(d2['A2'], '\n')

dct = {}
dct[(1, 2)] = 'Hello, Baby!'
dct[('One', 'Two')] = 'Python is awesome!'
print(dct, '\n')



# RGB
dct[(1, 2)] = 'Hello, Baby2!!'
print(dct, '\n')

paris = [('IBM', 125), ('ACME', 50), ('PHP', 40)]
d = dict(paris)

print(d, '\n')



# Structures
human = {"name": "Alex",
         "last name": "Docktor",
         "ahe": 19,
         "address":
             {"street": "Silicon",
              "house": 34,
              "flat": 1407}
         }
house = human["address"]["house"]
print(human)
print(house, '\n')

human["address"]["flat"] = 1408
print(human, '\n')

a = [{"name": "Alex", "last name": "Docktor", "ahe": 19}, {"name": "Veronika", "last name": "Mahas", "ahe": 19}]
print(a[1]["name"], '\n')



# digits methods

# .clear
gender_dict = {0: "Man", 1: "Woman"}
gender_dict.clear()
print(gender_dict, '\n')



# .copy
gender_dict = {0: "Man", 1: "Woman"}
gender_dict2 = gender_dict.copy()
print(gender_dict2)

gender_dict2[0] = "Man-Woman"
print(gender_dict)
print(gender_dict2)

print('gender1: ', id(gender_dict))
print('gender2: ', id(gender_dict2), '\n')

# a = {"name": {1: "Jack", 2: "Veronika"}, "last name": "Docktor", "ahe": 19}

gender_dict = {0: {1: "Man", 2: "Alex"}, 1: "Woman"}
gender_dict2 = gender_dict.copy()

gender_dict2[0][1] = "Alex"
gender_dict2[0][2] = "Man"

print(gender_dict)
print(gender_dict2)
print(id(gender_dict2[0]) == id(gender_dict[0]), '\n')



# .fromcase
my_dict = dict.fromkeys(['one', 'two', 3])
print(my_dict)

my_dict = dict.fromkeys(['one', '2', 3], 10)
print(my_dict, '\n')

my_dict = {}
for key in [1, 2, 3]:
    my_dict[key] = []

my_dict[1].append("add")
print(my_dict)

my_dict = {key: [] for key in [1, 2, 3]}

my_dict[1].append("added")
print(my_dict, '\n')



# .get
print(my_dict.get(1))
print(my_dict.get(6))
print(my_dict.get(6, {}))
print(my_dict.get(6, "PIP"), '\n')

g = gender_dict2[0][1]
print(g, '\n')



# .items
gender_dict = {0: "Man", 1: "Woman"}
print(gender_dict.items())

lst = list(gender_dict.items())
print(lst[0]) #Not work!

a = gender_dict.get('address', {})
print(a.items())

for key, val in gender_dict.items():
    print(f'Key: {key}, value: {val}')
print('\n')

for pair in gender_dict.items():
    print(f'Key: {pair[0]}, value: {pair[1]}')
print('\n')


# .keys
lst = gender_dict.keys()
print(list(lst)[1])

for key in gender_dict:
    print(f'Key: {key}')
print('\n')



# .values
print(gender_dict.values())
print("Alex" in gender_dict.values(), '\n')



# .pop
g = gender_dict.pop(1)
print(g)
print(gender_dict)

g = gender_dict.pop(1, {})
print(g, '\n')


# .popitem()
gender_dict = {0: "Man", 1: "Woman"}
k, v = gender_dict.popitem()
print(gender_dict)
print(k, v)



# .setdefault
dict_one = {}
lst = [1, 2, 3, 4, 5, 3, 1, 6]

for i in lst:
    count = dict_one.get(i, {})
    if count:
        dict_one[i] = count + 1
    else:
        dict_one[i] = 1

print(dict_one, '\n')



dict_one = {}
lst = [1, 2, 3, 4, 5, 3, 1, 6]

for i in lst:
    dict_one.setdefault(i, 0)

    dict_one[i] += 1

print(dict_one, '\n')



dict_one = {}
lst = [1, 2, 3, 4, 5, 3, 1, 6]

for i in lst:
    # dict_one.setdefault(i, 0)

    dict_one[i] = dict_one.get(i, 0) + 1


print(dict_one, '\n')



# my_dict = {}
# my_dict.setdefault(key, "One")
# # my_dict.setdefault(key, []).append(4)
#
#
# print(my_dict)




