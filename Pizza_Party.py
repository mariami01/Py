while True:
    try:
        people = int(input("How many people? "))
    except ValueError:
        people=input("Only numbers are allowed!: ")
    try:
        pizza = int(input("How many pizzas do you have? "))
    except ValueError:
        pizza = input("Only numbers are allowed!: ")
    finally:
        print(f"{people} people with {pizza} pizzas")
        pizza=int(pizza)
        people=int(people)
        if people <  pizza *8:
            pieces = (pizza*8) // people
            leftover = (pizza*8) % people
        elif (pizza *8)<people:
            pieces = people // (pizza*8)
            leftover = people % (pizza*8)

        print(f"Each person gets {pieces} pieces of pizza")
        print(f"There are {leftover} leftover pieces.")



