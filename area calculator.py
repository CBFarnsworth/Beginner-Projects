
import math

shape = input("Would you like to find the area of a Square, Triangle, or Circle?: ")

if shape == "Square":
    side = float(input("What is the length of one of it's sides?: "))
    Areas = pow(side,2)
    print(f"The area of your square is {Areas}")
elif shape == "Triangle":
    base = float(input("What is the length of it's base?: "))
    height = float(input("What is it's height?: "))
    Areat = base * height / 2
    print(f"The area of your triangle is {Areat}")
elif shape == "Circle":
    radius = float(input("What is it's radius?: "))
    Areac = math.pi * pow(radius, 2)
    print(f"The area of your circle is {round(Areac, 2)}")
else:
    print("Make sure the first letter is capatalized.")