def password_validation(password):
    if len(password)<6:
        print("Length should be at least 6")
        val = False
    if len(password)>20:
        print("Length should be maximum 20")
        val = False
    if not any(char.isdigit() for char in password):
        print("The password should have at least one digit")
        val = False
    if not any(char.isupper() for char in password):
        print("The password should have at least one uppercase letter")
        val = False
    if not any(char.islower() for char in password):
        print("The password should have at least one lowercase letter")
        val = False


user = input("What is the password? ")
password = 'Python01'
if password_validation(password):
    print("Welcome!")
else:
    print("I don't know you!")
