import math
try:
    p = int(input("What is the principal? "))
    r = float(input("What is the rate? "))
    t = int(input("What is the number of years? "))
    n = int(input("What is the number of times the interest is compounded per year? "))

    a = p*(1+(r*t))
    a = math.floor(a)
    print(f"{p} invested at {r}% for {t} years\ncompounded {n} times per year is ${a}.")
except Exception as e:
    print("Something went wrong!Try again later!")
