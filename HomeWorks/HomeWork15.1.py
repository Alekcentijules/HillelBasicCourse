class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        # return self.width * self.height
        return round(self.width * self.height, 5)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            # return self.get_square() == other.get_square()
            return round(self.get_square(), 5) == round(other.get_square(), 5)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            area = self.get_square() + other.get_square()
            # sd_width = int(area ** 0.5) + 1
            # sd_height = area // sd_width
            # return Rectangle(sd_width, sd_height)
            # for sd_width in range(1, int(area ** 0.5) + 1):
            #     if area % sd_width == 0:
            #         sd_height = area // sd_width
            #         return Rectangle(sd_width, sd_height)
            sd_width = self.width
            # sd_height = area / sd_width
            sd_height = round(area / sd_width, 5)
            return Rectangle(sd_width, sd_height)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)) and n > 0:
            area = self.get_square() * n
            # thd_width = int(area ** 0.5) + 1
            # thd_height = area // thd_width
            # return Rectangle(thd_width, thd_height)
            # if isinstance(n, (int, float)):
            # area = int(self.get_square() * n)
            # for thd_width in range(1, int(area ** 0.5) + 1):
            #     if area % thd_width == 0:
            #         thd_height = area // thd_width
            #         return Rectangle(thd_width, thd_height)
            thd_width = self.width
            # thd_height = area / thd_width
            thd_height = round(area / thd_width, 5)
            return Rectangle(thd_width, thd_height)
        return NotImplemented

    def __str__(self):
        return f"Rectangle [ width = {self.width}, height = {self.height}, area = {self.get_square()} ]"


# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# print(r1)
# print(r2)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# print(r3)
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# print(r4)
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

r1 = Rectangle(2.4, 4)
r2 = Rectangle(3, 6)

print(r1)
print(r2)
# Test1
assert r1.get_square() == 9.6, "Test1 failed"
# Test2
assert r2.get_square() == 18, "Test2 failed"

# Test3: Складання прямокутників
r3 = r1 + r2
print(r3)
assert r3.get_square() == 27.6, "Test3 failed"
print('OK')

















