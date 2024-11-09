user = int(input("Enter five-digit number: "))

div, mod = divmod(user, 10000)
div2, mod2 = divmod(mod, 1000)
div3, mod3 = divmod(mod2, 100)
div4, mod4 = divmod(mod3, 10)


result = mod4 * 10000 + div4 * 1000 + div3 * 100 + div2 * 10 + div
print("Your result: ", result)






