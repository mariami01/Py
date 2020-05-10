length = float(input("What is the length of the room in feet? "))
width = float(input("What is the width of the room in feet? "))
if not length.is_integer() or not width.is_integer():
    raise Exception ("All the values must be number!")

area = length *width
m = area / 3.28
print(f"You entered dimensions of {length} feet by {width} feet.")
print(f"The Area is\n{area} square feet")
print(f"{m} square meters")
