try:
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    for x, y in prices.items():
      print(x)
      print("price:",y)
      print("stock:", 0)
      print("____________________")


    for x,y in prices.items():
        try:
            stock = input(f'Enter the stock of the {x} : ')
        except ValueError:
            print("Wrong input!")


    total = 0
    for i in prices:
        total += prices[i] * stock[i]

    print("Totall: ", total)
except:
    print("Sorry, Something went wrong!")
