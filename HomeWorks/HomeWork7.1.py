def say_hi(name, age):
  return f"Hi. My name is {name} and I'm {age} years old!"

user_input_name = input("Enter a name: ")
user_input_age = int(input("Enter a age: "))

result = say_hi(user_input_name, user_input_age)
print(result)

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old!", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old!", 'Test2'
print('ОК')










