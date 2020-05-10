string = input("What is the input string? ")
if not string.isalpha():
    raise TypeError("Only Letters are allowed")

print(f"{string} has {len(string)} characters.")

