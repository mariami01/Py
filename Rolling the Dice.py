import random
import os
import sys

#clear screen

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# display rolls, and money

def display(money,roll,comp_roll):
    clear()
    print("Money: ${}".format(money))

    if roll == comp_roll:
        print("You win!")
    else:
        print("You lose!")


    print("The computer rolled a {}".format(comp_roll))
    print('')

    print("You rolled a {}".format(roll))
    print('')

#game begins

def play(done, money):
    clear()

    while True:

        roll = random.randint(1,6)
        comp_roll = random.randint(1,6)

        try:
            bet = int(input("How much money would you like to bet? "))
        except ValueError:
            print("That is not a number")
        else:
            if roll == comp_roll:
                money += bet
                display(money,roll,comp_roll)
                done = True
            else:
                money -= bet
                display(money,roll,comp_roll)
                done = True

            if money < 1:
                print("Sorry, looks like I took all your money.")
                print('')
                game_over = input("If you want I can lend you $1000 more dollars and we can play again? Y/n ")
                if game_over != 'n':
                    money = 1000
                    play(done,money)
                else:
                    print('Bye!')
                    sys.exit()

            if done:
                play_again = input('Would you like to play again? Y/n ').lower()
                if play_again != 'n':
                    done = False
                else:
                    sys.exit()

# welcome

def welcome():
    print("Welcome to Dice Roller, a game where you and the computer both roll dice.\nYou can also place bets. If you roll the same number, you win, if you roll different numbers you lose. You begin with $1000.")
    print('')
    start = input('Press enter/return to start or Q or quit ').lower()
    if start == 'q':
        print('Bye!')
        sys.exit()

done = False
money = 1000
while True:
    clear()
    welcome()
    play(done,money)
