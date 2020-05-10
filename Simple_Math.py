x = float(input("What is the first number? "))
y = float(input("What is the second number? "))

if not x.is_integer() or not y.is_integer():
    print("Values must be numbers!")

print(f"{x} + {y} = ", x + y)
print(f"{x} - {y} = ", x - y)
print(f"{x} * {y} =", x * y)
print(f"{x} / {y} =", x / y)
