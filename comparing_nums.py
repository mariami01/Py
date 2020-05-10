num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1 !=num2 and num2 !=num3:
    if num1>num2 and num1>num3:
        print(f"The Largest number is {num1}.")
    elif num2>num1 and num2>num3:
        print(f"The largest number is {num2}.")
    elif num3>num2 and num3>num1:
        print(f"The largest number is {num3}.")
else:
    print("All the numbers must be different from each other!")
