''' 
    Rock Paper Scissors
    Creator: Michael Scott
'''
from random import randrange

game_options = ["rock", "paper", "scissors"]

def welcome():
    print("Welcome to my Rock Paper Scissors game written in Python")
    print("Here are your choices")
    '''
        Managing exception errors with try and except statements
        It will try to get an int input from user 1, 2, or 3
        Exception error will be thrown if user input is invalid
    ''' 
    try:
        begin = int(input("\t1 = Play\n\t2 = Rules\n\t3 = Quit\n"))
        start(begin)
    except:
        print("Invalid input. Please try again.")
        welcome()
            
    #print("Invalid Input. Please try again.")
    #welcome()

def start(user_input):
    if user_input in range(1,4):
        if user_input == 1:
            play()
        elif user_input == 2:
            rules()
        else:
            quit_game()
    #else:
    #    print("Your input was " + str(begin) + ". You'll have to try again.")
    #    welcome()
    # print(choices(game_options))

def play():
    # computer chooses from game option list
    computer_choice = randrange(0,3)
    print("This is a random number " + str(computer_choice))
    # user's choice
    print("Your choices are:\n")
    user_choice = int(input("\t1 = rock\n\t2 = paper\n\t3 = scissors\n"))
    if user_choice == 1:
        print("You chose Rock")
        print("The computer chose " + game_options[computer_choice])
    elif user_choice == 2:
        print("You chose Paper")
        print("The computer chose " + game_options[computer_choice])
    elif user_choice == 3:
        print("You chose Scissor")
        print("The computer chose " + game_options[computer_choice])
    else:
        print("Opps... Invalid input... Please try again...")
        play()

'''
def logic(user_logic):
    for item in game_options:
        if item == user_logic:
            print("It's a tie")
            play()
        else:
            if item == "rock":
                print("You win!")
            elif item == "paper":
                print("You lose!")
'''


def rules():
    print("Testing out funciton.")


def quit_game():
    print("Testing out funciton.")


welcome()