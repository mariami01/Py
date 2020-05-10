def divisibility_3(n):
    return ''.join([i for i in n if int(i) %3 ==0])

def greater_5(n):
    return ''.join([str(int(i) //2) if int(i)>5 else i for i in n])

def no_odd(n):
    return ''.join([i for i in n if int(i) % 2 == 0])

def less_odd(n):
    return ''.join([str(int(i)-1) if int(i) % 2 != 0 else i for i in n])

def only_odd(n):
    return ''.join([i for i in n if int(i) % 2 !=0])

def remove_divisibility_3(n):
    return ''.join([i for i in n if int(i) % 3 != 0])

def add_even_1(n):
    return ''.join([str(int(i)+1) if int(i) % 2 == 0 else i for i in n])

def only_even(n):
    return ''.join([i for i in n if int(i) % 2 ==0])

def less_than_5(n):
    return ''.join([i for i in n if int(i) < 5])

def no_even(n):
    return ''.join([i for i in n if int(i) % 2 != 0])


def final ():

    try:
        num = input("Enter the integer number: ")
        print(" ")
        if num.isdigit():
            print(" ")
        else:
            print("You MUST enter only numbers!")
        try:

            print("დატოვეთ 3 ის ჯერადი ციფრები:", divisibility_3(num))
        except ValueError:
            print("Something Wrong!")

        try:
            print("ციფრები, რომელიც მეტი არის 5 ზე გაყავით 2 ზე:", greater_5(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("ამოშალეთ კენტი ციფრები:", no_odd(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("კენტი ციფრებს გამოაკელით 1:", less_odd(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("დატოვეთ კენტი ციფრები:", only_odd(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("ამოშალეთ 3 -ს ჯერადი ციფრები:", remove_divisibility_3(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("დაუმატეთ ლუწ ციფრებს 1:", add_even_1(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("დატოვეთ ლუწი ციფრები:", only_even(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("დატოვეთ ციფრები, რომლებიც ნაკლებია 5 ზე:", less_than_5(num))
        except ValueError:
            print("Something Wrong!")
        try:
            print("ამოშალეთ ლუწი ციფრები:", no_even(num))
        except ValueError:
            print("Something Wrong!")
    except:
        print("Sorry!Something went wrong!")
final()



