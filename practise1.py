# Print Hello World
print("hello world")

#Take two integers as input from the user and print their sum
a=int(input("1st no:"))
b=int(input("2nd no:"))
print("sum:", a + b)

#take the side length of a square as input and print its area.
a=float(input("side:"))
print("area:", a**2)

#Take two floating-point numbers as input and print their average
a=float(input("a:"))
b=float(input("b:"))
print("average:", (a+b) /2) 

#take two integers as input and print True if the first number is greater than or equal to the second number; otherwise print False.

a, b=9, 5
print(a>=b)

#Take two numbers as input and print the remainder when the first number is divided by the second.
a, b=15, 2
print(a % b)

#take a number as input using input(), convert it to an integer, add 10, and print the result.
a=input("enter a number:")
b=int(a)
print("result:", b + 10)

#Create variables of type int, float, str, and bool, then print their data types using the type() function.
a=10
b=3.2
c="piyush"
d=True
print(type(a),
          type(b), 
            type(c),
              type(d))

#Create variables: and do arithmatic operation
a, b= 2, 5
print("add:", a + b)
print("sub:", a - b)
print("mul:", a * b)
print("div:", b/a)
print("power:", b**a)

#Take the user's name as input and print
a=input("enter your name :")
print("Welcome", a)
