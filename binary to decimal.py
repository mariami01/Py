def check_binary():
    binary = "01"
    string = input("Enter binary number with 8 digits: ")
    if string.isdigit() and len(string) == 8:
        for i in string:
            if i not in binary:
                return check_binary()
        return string
    else:
        return check_binary()


def binaryToDecimal():
        for i in range(len(string)):
            digit = string.pop()
            if digit == '1':
                value1 = value + pow(2, i)
                print("The decimal value of the number is", value)

print("The decimal value of the number is", value1)
