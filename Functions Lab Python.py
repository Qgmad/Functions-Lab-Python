import math
from datetime import date
#Q1
def mul(a,b):
    c=a*b
    return(c)

a=int(input("Enter the first value"))
b=int(input("Enter the Second value"))
c=mul(a,b)
print(c)

#Q2
def mul(a,b):
    c=a+b
    return(c)

a=int(input("Enter the first value"))
b=int(input("Enter the Second value"))
c=mul(a,b)
print(c)

#Q3

def fact(a):
    fact=1
    for i in range(a,0,-1):
        fact=fact*i
    return (fact)

a=int(input("Enter The Number"))
b=fact(a)
print(b)

#Q4

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
a=int(input("Enter The Number To cal fabonacii"))
print(fibonacci(a))

#Q5
def swap(a,b):
    temp=a
    a=b
    b=temp
    print("value of a and b after swapping",a,b)
a=int(input("Enter The first Number"))
b=int(input("Enter The Second Number"))
print("before swapping value of a,b is ",a,b)
swap(a,b)

#Q6
def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

a=int(input("Enter The first Number"))
b=int(input("Enter The Second Number"))

print("The H.C.F. is", hcf(a,b))

#Q7
def asciival(n):
    print("Ascii value of ' " + n + "' is",ord(n))

a=input("Enter a character")
asciival(a)

#Q8
a=int(input("Enter The first Number"))
b=int(input("Enter The Second Number"))

print(math.pow(a,b))
print(math.sqrt(a))
print(math.log10(b))

#Q9
today = date.today()
print("Today's date is", today)
#Q10
def greet(name,msg):
   print("Hello",name + ', ' + msg)

greet(ABC","Good morning!")
"""IN THIS FUNCTION WE REQUIRE 2 ARGUMENT"""

#Q10
def greet(name,msg):
   print("Hello",name + ', ' + msg)

greet(name = "Mayank",msg = "How do you do?")

#Q11
def greet(name, msg = "Good morning!"):

   print("Hello",name + ', ' + msg)

greet("Prince")
greet("Mayank","How do you do?")

#Q12
def greet(*names):
   for name in names:
       print("Hello",name)

greet("ABC","DEF","GHI","JKL")
