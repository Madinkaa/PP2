#Write a Python program to convert degree to radian
import math
degree = float(input("Input degree:"))
radian = math.radians(degree)
print("Output radian:", radian)

#Write a Python program to calculate the area of a trapezoid
import math
hight = int(input("Hight: "))
first = int(input("Base, first value: "))
second = int(input("Base, second value: "))
s = ((first + second) * hight) / 2
print("Expected Output:" , s)

#Write a Python program to calculate the area of regular polygon
import math
n = int(input("Input number of sides:"))
s = int(input("Input the length of a side:"))

area = int((0.25 * n * s**2) / math.tan(math.pi / n))
print("The area of the polygon is:", area )

"""def polygon(n, s):
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    return area

n = int(input("Input number of sides:"))
s = int(input("Input the length of a side:"))

area = polygon(n, s)
print("The area of the polygon is:", area )
"""
#Write a Python program to calculate the area of a parallelogram
import math
a = int(input("Length of base:"))
h = int(input("Height of parallelogram:"))
s = float(a  * h)
print("Expected Output:", s)