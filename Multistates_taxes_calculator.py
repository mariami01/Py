amount = float(input("What is the order amount? "))
state = input("What is the state you live in? ")
if state == 'Wisconsin' or state=='winsconsin':
    tax = 0.50
    country=input("Choose the resident country - Eua Clare or Dunn:  ")
    if country=='Eua Clare' or country=='eua clare':
        total_tax=0.005+tax
        total=total_tax+amount
        print(f"The tax is ${total_tax}.")
        print(f"The total is ${total}.")
    elif country=='Dunn' or country=='dunn':
        total_tax=0.004+tax
        total=total_tax+amount
        print(f"The tax is ${total_tax}.")
        print(f"The total is ${total}.")
elif state == 'Ilinois'or state=='ilinois':
    tax=0.008
    total=tax+amount
    print(f"The tax is ${tax}.")
    print(f"The total is ${total}.")

else:
    tax=0.50
    total=tax+amount
    print(f"The tax is ${tax}.")
    print(f"The total is ${total}.")
