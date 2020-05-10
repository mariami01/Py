def the_day(d,m,c,y):
    return ((d+((13*m-1)//5))+y+(y//4)+(c//4)-2*c+777)%7

try:
    month = int(input("Enter the month as a number\nJanuary(1), February(2), March(3), April(4), May(5), June(6), July(7),\nAugust(8), September(9), October(10), November(11), December(12): "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))

    print("The next day is", the_day(day,month,year%1000,year%100))
except Exception as e:
    print("Something went wrong!try again,later!")
