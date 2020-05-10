try:
    price1 = float(input("Enter the price of item 1: "))
    quantity1 = float(input("Enter the quantity of item 1: "))
    total1=price1*quantity1

    price2 = float(input("Enter the price of item 2: "))
    quantity2 = float(input("Enter the quantity of item 2: "))
    total2=price2*quantity2

    price3 = float(input("Enter the price of item 3: "))
    quantity3 = float(input("Enter the quantity of item 3: "))
    total3=float(price3)*float(quantity3)

    subtotal = total1 + total2 + total3
    tax = (subtotal* 5.5)/100
    total = subtotal + tax
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")


except ValueError:
    print("Only numbers are allowed!")


