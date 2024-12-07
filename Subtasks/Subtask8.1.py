import math

def calculate_circle_area(radius):
    # pi_ = math.pi
    a = math.pi * (radius ** 2)
    return a

user_input_radius = float(input("Enter a radius: "))
result = calculate_circle_area(user_input_radius)

print(result)















