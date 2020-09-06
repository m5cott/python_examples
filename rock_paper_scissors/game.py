''' 
    Rock Paper Scissors
    Creator: Michael Scott
'''
from random import randrange

game_options = ["rock", "paper", "scissors"]

def welcome():
    print("Welcome to my Rock Paper Scissors game written in Python")
    print("Here are your choices\n")
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
            
def start(user_input):
    if user_input in range(1,4):
        if user_input == 1:
            play()
        elif user_input == 2:
            rules()
        else:
            quit_game()
    else:
        print("Your input was " + user_input + ". You'll have to try again.")
        welcome()

def play():
    # computer chooses from game option list
    computer_choice = randrange(0,3)

    # user's choice
    print("Your choices are:\n")
    user_choice = int(input("\t1 = rock\n\t2 = paper\n\t3 = scissors\n"))
    user_choice-=1
    if user_choice == 0:
        print("You chose Rock")
        print("The computer chose " + game_options[computer_choice])
        logic(user_choice, computer_choice)
    elif user_choice == 1:
        print("You chose Paper")
        print("The computer chose " + game_options[computer_choice])
        logic(user_choice, computer_choice)
    elif user_choice == 2:
        print("You chose Scissor")
        print("The computer chose " + game_options[computer_choice])
        logic(user_choice, computer_choice)
    else:
        print("Opps... Invalid input... Please try again...")
        play()

def logic(user_logic, game_logic):
    if user_logic == game_logic:
        print("It's a tie. The computer chose " + game_options[game_logic] + " and you chose " + game_options[user_logic])
        welcome()
    
    if user_logic == 0: # Rock
        if game_logic - 2 != 0:
            print("You lose! " + game_options[game_logic] + " beats " + game_options[user_logic])
            welcome()
        else:
            print("You win! " + game_options[user_logic] + " beats " + game_options[game_logic])
            welcome()    
    elif user_logic == 1: # Paper
        if user_logic < game_logic:
            print("You lose! " + game_options[game_logic] + " beats " + game_options[user_logic])
            welcome()
        else:
            print("You win! " + game_options[user_logic] + " beats " + game_options[game_logic])
            welcome()
    elif user_logic == 2: # Scissors
        if user_logic - 1 == game_logic:
            print("You win! " + game_options[user_logic] + " beats " + game_options[game_logic])
            welcome()
        else:
            print("You lose! " + game_options[game_logic] + " beats " + game_options[user_logic])
            welcome()
        

def rules():
    print("Here are the rules...\n")
    print("\tRock crushes scissors\n\tPaper covers rock\n\tScissors cuts paper\n")
    welcome()


def quit_game():
    quit()


welcome()