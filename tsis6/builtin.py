#Write a Python program with builtin function to multiply all the numbers in a list
def list(num):
    k = 1
    for n in num:
        k *= n
    return k

my_list = [1, 3, 4, 5]
m = list(my_list)
print(m)

#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_upper_lower(string):
    lower = 0
    upper = 0
    for char in string:
        if char.islower():
            lower += 1
        if char.isupper():
            upper += 1
    print(f"The number of lowercase characters is: {lower}")
    print(f"The number of uppercase characters is: {upper}")

string = input()
count_upper_lower(string)

#Write a Python program with builtin function that checks whether a passed string is palindrome or not
def is_palindrome(s):
    return s == s[::-1]

input_string = "malayalam"
if is_palindrome(input_string):
    print("Yes")
else:
    print("No")


# Write a Python program that invoke square root function after specific milliseconds
from time import sleep
import math

def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)
print("Square root after specific milliseconds:")

print(delay(lambda x: math.sqrt(x), 3000, 16))

print(delay(lambda x: math.sqrt(x), 5000, 100))

print(delay(lambda x: math.sqrt(x), 7000, 25100))


#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def are_all_elements_true(my_tuple):
    return all(my_tuple)

my_tuple1 = (True, True, True)
result1 = are_all_elements_true(my_tuple1)
print(f"Are all elements of the first tuple true? {result1}")

my_tuple2 = (True, True, False)
result2 = are_all_elements_true(my_tuple2)
print(f"Are all elements of the second tuple true? {result2}")


import math
def square_area(side_length):
    return side_length ** 2

side_length = 5 
area = square_area(side_length)  

print("Площадь квадрата:", area)
