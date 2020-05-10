def cylinder_volume(r,h):

    if (not str(r).isdigit()) or (not str(h).isdigit()):
        raise Exception("The radius and the height must be a number!")
    elif float(r)<=0 or float(h)<=0:
        raise Exception("The radius and the height  must be positive!")
    else:
        return 3.14*float(r)*float(r)*float(h)


try:
    r = input("Enter the radius of the cylinder: ")
    h = input("Enter the height: ")
    result = cylinder_volume(r,h)
    print("The volume of the cylinder is ",result)
except Exception as e:
    print(e.args[0])

