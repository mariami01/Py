home = input("Are you at home?(y/n): ")

if home.isalpha():
    if home == "y":
        print("Good :) Stay There ! ")
    else:
        print("Go to the home")
        print(" ")
        home_1 = input("Are you at home now?(y/n): ")
        if home_1 == "y":
            print("Good :) Stay There ! ")
        else:
            print("Go to the home! ")


else:
    print("Wrong input!")
