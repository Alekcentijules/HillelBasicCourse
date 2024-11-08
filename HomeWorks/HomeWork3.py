user = int(input("Enter five-digit number: "))

div, mod = divmod(user, 10000)
div2, mod2 = divmod(mod, 1000)
div3, mod3 = divmod(mod2, 100)
div4, mod4 = divmod(mod3, 10)
div5, mod5 = divmod(mod4, 1)

result = div5 * 10000 + div4 * 1000 + div3 * 100 + div2 * 10 + div
print(result)






