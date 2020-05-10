order = input("What is the order amount? ")
state = input("What is the state? ")


if state == 'WI':
    tax = (int(order)*5.5)/100
    total = tax + int(order)
    print(f"The subtotal is {float(order)}.")
    print(f"The tax is {float(tax)}.")
    print(f"The total is {float(total)}.")
elif state !='WI':
    print(f"The total is {float(order)}.")

