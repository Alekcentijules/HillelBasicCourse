# OrderedDict

# .popitem()



# .move_to_end()



# defaultdict



# namedtuple

from collections import namedtuple

fields = ('color', 'engine')
car = namedtuple('Car', fields)
car1 = car('red', 2000)

print(car1[0])
print(car1.engine)
print(car, '\n')


Point = namedtuple('Point', ['x', 'y'])
p = Point(12, 23)

print(p.x)
print(p.y)

data_dict = {"x": 56, "y": 67}
p2 = Point(**data_dict)

print(p2)



# Set



# Methods

# add()



# set.update()



# .difference()



# .symmetric_difference()



# .difference_update()



# .discard()



# .remove()



# .clear()



# .pop()



# .union(x, y, z)



# .infersection()



# .infersection_update()



# .copy()



# .issubset()



# issuperset()



# .isdisjoint()



# Function



# len()



# all()



# any()



# max(), min(), sum()



# sorted()



# enumerte()



# Frozenset



# Functions



# def



# assert



# return




















