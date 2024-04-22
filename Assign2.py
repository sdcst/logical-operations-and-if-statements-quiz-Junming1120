"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
a = float(input("enter the length of a: "))
b = float(input("enter the length of b: "))
d = str(input("which one is the hypotenuse of a right triangle? "))
if d == "a":
    c = ((a**2)-(b**2))**0.5
    c = round(c,1)
    print(f"the missing side is {c}")
elif d =="b":
    c = ((b**2)-(a**2))**0.5
    c = round(c,1)
    print(f"the missing side is {c}")
else:
    c = ((a**2)+(b**2))**0.5
    c = round(c,1)
    print(f"the hypotenuse side is {c}")