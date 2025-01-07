# bubble_sort



# time



# open



# write and writeliness



# close



# enumerete



# codecs



# seek



# with



# shelve



# openpyxl



# OOP



import os


# with open("C:/Users/ohala/Downloads/draft.html", "r", encoding="utf-8") as file:
#     cont = file.read()
# print(cont)


# with open("C:/Users/ohala/Downloads/draft.html", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())


# with open("C:/Users/ohala/Downloads/draft.html", "r", encoding="utf-8") as file:
#     lines = file.readline()
#     # for line in lines:
#     #     print(line)
#     print(lines)
#     print(type(lines))


with open("Test.py", "w", encoding="utf-8") as file:
    file.write("It's a new string!.\n")
    file.write("Adding another one string.\n")
    file.write("Adding another one string.\n")
    # f = file.read()



# with open("Test.py", "a", encoding="utf-8") as file:
#     file.write("This string added to end!\n")



# with open("Test.py", "r", encoding="utf-8") as file:
#     r = file.read()
#     print(r)



with open("Test.py", "r+", encoding="utf-8") as file:
    file.seek(0, 2)
    file.write("This string added to end!\n")
    file.seek(0)
    r = file.read()
    print(r)



# with open("Test.py", "rb", encoding="utf-8") as file:
#     content = file.read()
#     print(content[:20])



# data = b"Hello, Im binary string!"
# with open("Test.py", "wb", encoding="utf-8") as file:
#     file.write(data)



# with open("Test.py", "r", encoding="utf-8") as file:
#     r = file.read()
#     print(r)



print(os.path.exists("Test.py"))



# os.mkdir("Test_Folder")

print(os.listdir("."))




