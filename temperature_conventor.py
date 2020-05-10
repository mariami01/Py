try:
    print("Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.")
    temp_type = input("Your Choice: ")

    while not temp_type.isalpha():
        temp_type = input("Only letters are allowed! Try again: ")

    if temp_type == 'c' or temp_type == 'C':
        temp1 = float(input("Please, Enter the temperature in Fahrenheit: "))
        c=(temp1-32)* (5/9)
        print(f"Temperature in Celsius is {c}.")

    elif temp_type == 'f' or temp_type == 'F':
        temp2 = float(input("Please, Enter the temperature in Fahrenheit: "))
        f=(temp2*(9/5)+32)
        print(f"Temperature in Fahrenheit is {f}.")
except Exception.args[0]:
    print("Wrong input!", Exception.args[0])
