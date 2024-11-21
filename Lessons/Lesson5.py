my_string = """I like
""Python"" """

print(my_string, '\n')



my_string = "I \"like\" Python"

print(my_string, '\n')



digits = str(23320)

print(digits)
print(type(digits), '\n')



lst = str(['O', 3, 3])

print(lst)
print(type(lst))
print(list(lst))



my_string = "Hello \n world"

print(my_string)
print(len(my_string))


my_string = "HO!" * 10

print(my_string)
print("-" * 35)



print(len("\n"))



my_string = "Python is awesome!"

print(my_string[7:-1], '\n')



my_string = my_string[:6] + 'N' + my_string[7:]

print(my_string)



print("like" in my_string, "\n")




# Methods

# .upper
my_string = "I like Python!"
my_string = my_string.upper()

print(my_string, '\n')



# .lower
my_string1 = my_string.lower()

print(my_string)
print(my_string1)

print("EwiW".lower() == "ewiw", '\n')



# .title
my_string = "Python is awesome!"
my_string = my_string.title()
print(my_string, '\n')



# .swapcase()
my_string = "Python is awesome!"
my_string = my_string.swapcase()
print(my_string, '\n')

print('|', my_string.ljust(20, "*"), '|', sep='')
print('|', my_string.rjust(20), '|', sep='')
print('|', my_string.center(20, "-"), '|', sep='')



# .replace
my_string = "Python is awesome!"
my_string = my_string.replace("Python", "Alex").replace("!", "!!!")
print(my_string, '\n')


# .split
my_string = "I like Python"
my_string = my_string.split("l")
print(my_string, '\n')

my_string = "I like Python"
my_string = my_string.split(" ")
print(my_string, '\n')

lst = " ".split("2")
print(lst, '\n')

my_string = '''I like 
Python'''
lst = my_string.split()
print(lst, '\n')



# .join
my_lst = ['I', 'like', 'Python']
_string = ''.join(my_lst)
print(_string, '\n')

my_str = "I like Python"
_string = '_'.join(my_str)
print(_string)

_string = "-".join("TTTT")
print(_string, '\n')

my_string = "I " + "like" + " Python"
print(my_string)

my_string = "-".join(my_string)
print(my_string, '\n')

lst = [2, 3, 5] # join працює тільки з типом даних "рядок"
# print("".join(lst))

x = ''.join([str(y) for y in lst])
print(x)
print(type(x), '\n')



# .strip
my_string = "   I like Python!          "
print(my_string)

my_string = my_string.strip()
print(my_string)

my_string = my_string.strip("!")
print(my_string, '\n')


# .r and lstrip
my_string = "@I like Python!"
print(my_string)

my_string = my_string.lstrip("@")
print(my_string)

my_string = my_string.rstrip("!")
print(my_string, '\n')

my_string = "   I like Python!          "
my_string = my_string.strip().strip("!").replace("i", "I")
print(my_string, '\n')



# %
my_string = "Hello %s! %s how are you?"
name = "Alex"
print(my_string % (name, name))

age = '19'
my_string = "Hello %s" # not %d
print(my_string % age, '\n')




# .format
name = "Anna"
my_string = "Hello {}"
print(my_string.format(name))

tmplt = "Hello, I am {0}. And my name is {1}"
text = tmplt.format("Alex", "Not Alex")
print(text)

text = "Hello, I am {}. And i am {} years old".format("Alex", 19)
print(text, '\n')

name = "Alex"
tmp = "Hello {name}{important}"
my_string = tmp.format(important="!", name=name)
print(my_string)

text = "Hello, I am {1}. I am {0} years old".format(36, "Alexander", 23)
print(text, '\n')

text = "Hello, I am {name}. I am {age} years old"
# Якщо аргументів буде більше, ніж потрібно, то це ні на що не вплине
print(text.format(age=36, name="Alexander", a=10))



# f-strings
name_1 = "Alex"
name_2 = "Veronika"
my_string = f"Hello {name_1.upper()}, {name_1 + name_2}, {name_2.title()}!"
print(my_string, '\n')



# math
import math
print(math.pi)
text = "Pi = {:.4f}".format(math.pi)
print(text, '\n')



# Padding
print("{}_v{:0{}d}".format('some string', 2153, 7))

print("{name}_v{val:0{dgt}d}".format(name='some string', val=1, dgt=6))

print('{}-------{:06d}'.format("name", 243))

print('{name}-------{val:0{dgt}d}'.format(name='some string', val=14, dgt=6), '\n')



# import this
import this
print()



# .find
my_str = "Beautiful is better"
ind = my_str.find("e")
print(ind)

ind = my_string.find("e", ind + 1)
print(ind)

print(my_string.find('e', 200), '\n')



# .count
print(my_string.count("e"), '\n')



# .isalpha
print(my_string.isalpha())

my_string = "Beautiful"
print("Isalpha: ", my_string.isalpha())



# .isdigit
my_string = '12345O'
print("Isdigit: ", my_string.isdigit())



# .isalnum
my_string = '12345!'
print("Isalnum: ", my_string.isalnum(), '\n')

text = "Happy new 2025 year!"
digits = 0

for i in text:
    if i.isdigit():
        digits += 1
        print(i, end="")
print()

print(digits, '\n')



# .count
text = "Happy new 2025 year!"
print(".count: ", text.count('2'))



# .isupper
text = "Happy new 2025 year!"
print(".isupper: ", text.isupper())



# .islower
print(".islower: ", text.islower())



# .starswith
print(".startswith: ", text.startswith("Ha"))



# .endswith
print(".endswith: ", text.endswith("ear"))



# .istitle
print(".istitle: ", text.istitle(), '\n')



# .zfill
string = '42'
s = string.zfill(5)
print(".zfill: ", s)

print('12323432Azis'.zfill(17))

print(str(4343).zfill(7), "\n")



# Module string
import string



# .ascii
print(".ascii_lowercase: ", string.ascii_lowercase)

print(".ascii_uppercase: ", string.ascii_uppercase)

print(".ascii_letters: ", string.ascii_letters, '\n')



# .punctuation
print(".punctuation: ", string.punctuation, '\n')



# .digits
print(".digits: ", string.digits, '\n')



# .hexdigits
print(".hexdigits: ", string.hexdigits, '\n')



# ASCII / UTF-8
text = "Flat is better than nested."
print("ASCII / UTF-8: ")
for letter in text:
    print(str(hex(ord(letter)).replace('0x', '')), end=' ')

print('\n')



# .ord
print(hex(53))
print(ord('A'))
print(ord("А"))
print("Alex == Alex", "Alex" == "Аlex", '\n')

for i in "Аlex":
    print(ord(i), end=" ")
print('\n')



# chr()
print("chr(): ", chr(1040))
print(chr(65), '\n')



# eval()
print("eval(): ", eval('120 + 4'), '\n')



# keyword.kwlist
import keyword

print(keyword.kwlist, '\n')






