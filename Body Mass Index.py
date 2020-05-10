order = input("Hello! If you need some help you are in a right place!\nWould you like to get recommendations regardless the weight?(y/n): ")

def severe_weight_deficiency(mass):
    return ''.join(str("Severe weight deficiency") if BMI < 16 else None)

def weight_deficiency(mass):
    return ''.join(str(print("Weight deficiency")) if 16 < BMI < 18.5 else None)

def normal_weight(mass):
    return (str("Normal Weight") if 18.5 < BMI < 25 else None)

def excess_weight(mass):
    return (str("Excess weight") if 25 < BMI < 30 else None)

def obesity(mass):
    return (str("Obesity") if BMI > 30 else None)


if order == "y":
    m = float(input("Please, Enter your weight: "))
    h = float(input("Please, Enter your height(in metres): "))
    BMI = m/(h**2)
    normal_mass = 18.5 *h
    recomended_mass = m - normal_mass
    if BMI < 16:
        print("Your Body Mass Index is", BMI, "And it is", severe_weight_deficiency(m), "you must gain", recomended_mass, "kg")
    elif 16<BMI <18.5:
        print("Your Body Mass Index is", BMI, "And it is", weight_deficiency(m), "you must gain", recomended_mass, "kg")
    elif 25<BMI<30:
        print("Your Body Mass Index is", BMI, "And it is", excess_weight(m), "you must lose", recomended_mass, "kg")
    elif BMI>30:
        print("Your Body Mass Index is", BMI, "And it is", obesity(m), "you must lose", recomended_mass, "kg")
    else:
        print("Your Body Mass Index is", BMI,"\nYou have normal weight! Keep being healthy, cuz Greatest wealth is health! :)")
else:
    print("OK.")
