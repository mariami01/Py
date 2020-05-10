import math
try:
    p = int(input("Enter the principal: "))
    r = float(input("Enter the rate of interest: "))
    t = int(input("Enter the number of years: "))


    a = p*(1+(r*t))
    a = math.floor(a)
    print(f"After {t} years at {r}%,the investmnet will\nbe worth ${a}.")
except Exception as e:
    print("Something went wrong!Try again later!")
