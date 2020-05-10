import datetime
try:
    try:
        cur_age = int(input("What is your current age? "))
        ret_age = int(input("What is the age you like to retire? "))
    except Exception as e:
        print("Values must be digital!")

    till_retire = ret_age - cur_age
    now = datetime.datetime.now()
    ret_year = now.year + till_retire

    if till_retire > 0:
        print(f"You have {till_retire} years left until you can retire.")
        print(f"It's {now.year}, so you can retire in {ret_year}.")
    else:
        print(f"It's {now.year} and you should have retired in {ret_year}.")
except Exception as e:
    print("Sorry, something went wrong!")
