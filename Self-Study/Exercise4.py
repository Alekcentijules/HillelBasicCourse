user_input_celsius = float(input("Enter the temperature in degrees Celsius: "))

fahrenheit = user_input_celsius * (9 / 5) + 32
rounded_result = round(fahrenheit, 1)

print(f'Temperature in degrees Fahrenheit: {rounded_result}')
print(f'The method of rounding using f-string formating: {rounded_result:.1f}')
print('The method of rounding using format() method', "{:.1f}".format(rounded_result))

















