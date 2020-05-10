try:
    age  = int(input("What is your age? "))

    if age >=16:
        print("Congrats! You are old enough to legally drive ^_^ ")
    elif age <16:
        print("Sorry, you have to wait for a while. You aren't old enough to drive :(")
except (ValueError, ZeroDivisionError):
    print("Incorrect input!Please, try again later.")

