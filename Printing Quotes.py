quote = input("What is the quote? ")
author = input("Who said it? ")

if quote.isspace() and author.isspace() and not quote.isalpha() and not author.isalpha():
    print("Only Letters are allowed!")

print(f'{author} says, "{quote}" ')
