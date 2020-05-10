import math
def rectangular_area(leangth,width):
    return float(length)*float(width)

def round_area(pi,r):
    return r**2 *pi


def needed_gallon(area,x):
    return math.ceil(area/350)

shape = int(input("Choose the shape of a room from the options:\n1.rectangular. 2.round(1 or 2): "))

if shape == 1:
    length = float(input("Enter the Length: "))
    while not length.is_integer() or length <=0:
        length=input("Only (positive) numbers are allowed!Try again: ")

    width = float(input("Enter the width: "))
    while not width.is_integer() or length <=0:
        width=input("Only (positive) numbers are allowed!Try again: ")
    print("You will need to purchase ", rectangular_area(length,width), "gallons of\npaint to cover", needed_gallon(rectangular_area(length,width),350), "square feet")
elif shape == 2:
    radius = float(input("Enter radius: "))
    while not radius.is_integer() or radius <=0:
        radius = input("Only (positive) numbers are allowed!Try again: ")
    print("You will need to purchase ", round_area(3.14,radius), "gallons of\npaint to cover", needed_gallon(round_area(3.14,radius),350), "square feet")
