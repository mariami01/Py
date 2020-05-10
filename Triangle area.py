def triangle_area(a,h):
    if (not str(a).isdigit()) or (not str(h).isdigit()):
        raise Exception("The side and the height of the triangle must be a number!")
    elif float(a)<=0 or float(h)<=0:
        raise Exception("The side and the height of the triangle must be positive!")
    else:
        return 0.5*float(a)*float(h)

try:
    a = input("Enter the side of the triangle: ")
    h = input("Enter the height: ")
    result = triangle_area(a,h)
    print("The are of the triangle is ", result)
except Exception as e:
    print(e.args[0])

