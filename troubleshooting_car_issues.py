prob = input("Is the car silent when you turn the key?(y/n): ")
while not prob.isalpha():
    prob=input("Only letters are allowed!try again (y/n): ")

if prob=='y':

    battery=input("Are the battery terminals corroded?(y/n)")
    while not battery.isalpha():
        battery=input("Only letters are allowed!try again (y/n): ")
    if battery=='y':
        print("Clean terminals and try starting again.")
    elif battery=='n':
        print("Replace cables and try again.")
    else:
        pass

elif prob=='n':
    noise=input("Does the car make a clicking noise?(y/n): ")
    while not noise.isalpha():
        noise=input("Only letters are allowed!try again (y/n): ")
    if noise=='y':
        print("Replace the battery.")
    elif noise=='n':
        crank=input("Does the car crank up but fail to start?(y/n): ")
        while not crank.isalpha():
            crank=input("Only letters are allowed!try again (y/n): ")
        if crank=='y':
            print("Check spark plug connections.")
        elif crank=='n':
            engine=input("Does the car engine start and then die?(y/n): ")
            while not engine.isalpha():
                engine=input("Only letters are allowed!try again (y/n): ")
            if engine=='y':
                fuel=input("Does your car have fuel injection?(y/n)")
                while not fuel.isalpha():
                    fuel=input("Only letters are allowed!try again (y/n): ")
                if fuel=='y':
                    print("Get it for service.")
                elif fuel=='n':
                    print("Check to ensure the choke is opening and closing.")
                else:
                    pass
    else:
        pass
else:
    pass
