#Create a generator that generates the squares of numbers up to some number N
def generator(N):
    for i in range(N):
        yield i**2

n = int(input())
squares = generator(n)
for num in squares:
    print(num)

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def generator(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i

n = int(input())
even = generator(n)
res = ",".join(str(num) for num in even)
print(res)

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def generator(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
even = generator(n)
res = ",".join(str(num) for num in even)
print(res)

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def generator(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = int(input())
b = int(input())
square = generator(a, b)
for num in square:
    print(num)

#Implement a generator that returns all numbers from (n) down to 0
def generator(n):
    for i in range(0, n):
        yield i

n = int(input())
square = generator(n)
for num in square:
    print(num)