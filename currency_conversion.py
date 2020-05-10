import math
euro = input("How many euros are you exchanging? ")
while not euro.isdigit():
    euro = input("Only numbers are allowed!Try again: ")
euro_rate = input("What is the exchange rate? ")
while not euro_rate.isdigit():
    euro_rate = input("Only numbers are allowed!Try again: ")


def currency(euro,euro_rate):
    usd_rate=1.8
    euro = float(euro)
    euro_rate = float(euro_rate)
    usd = (euro*euro_rate)/usd_rate
    return math.floor(usd)

print(f"{euro} euros at an exchange rate of {euro_rate} is\n{currency(euro,euro_rate)} U.S. dollars.")
