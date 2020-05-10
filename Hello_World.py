name = input("What is your name? ")
if not name.isalpha():
    raise TypeError("Only Letters are allowed")

print(f"Hello, {name}, Good to see you!")

