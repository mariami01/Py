try:
    w = float(input("Enter your body weight in pounds: "))
    h = float(input("Enter number of hours since last drink: "))
    a = float(input("How many drink were consumed?(oz): "))
    gender = input("Enter your gender(female/male): ")
    while not gender.isalpha():
        gender = input("You can only enter letters.Please, try again: ")

    if gender=='female':
        r1=0.73
        bac = ((a*5.14)/(w*r1))-0.015*h
        if bac>=0.08:
            print(f"Your BAC {bac}\nIt's not legal for you to drive.")
        elif bac<0.08:
            print(f"Your BAC {bac}\nIt's  legal for you to drive.")
    elif gender=='male':
        r=0.66
        bac = (a*5.14/w*r)-0.015*h
        if bac>=0.08:
            print(f"Your BAC {bac}\nIt's not legal for you to drive.")
        elif bac<0.08:
            print(f"Your BAC {bac}\nIt's  legal for you to drive.")

except(ValueError,TypeError,ZeroDivisionError):
    print("Sorry, your input isn't right. Please,try again :)")
