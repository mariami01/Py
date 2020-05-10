def switch_month(arg):
    switcher={
        1:  "January",
        2:  "February",
        3:  "March",
        4:  "April",
        5:  "May",
        6:  "June",
        7:  "July",
        8:  "August",
        9:  "September",
        10: "Octomber",
        11: "November",
        12: "December"
    }
    print(switcher.get(arg,"Invalid Month"))

month = input("Please, enter the number of the month: ")
print("The name of the month is")
print(switch_month(3))
