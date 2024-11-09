user = int(input("Enter four-digit number: "))

div, mod = divmod(user, 1000)
print(div)
div2, mod2 = divmod(mod, 100)
print(div2)
div3, mod3 = divmod(mod2, 10)
print(div3)
print(mod3)