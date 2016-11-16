# Guess A Number AI
#
# Ian Thompson
# September 1, 2016

import random
import math


def start():
    print("  _____                               _   _                 _   ")            
    print(" / ____|                             | \ | |               | |       ")       
    print("| |  __ _   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __") 
    print("| | |_ | | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|")
    print("| |__| | |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |")   
    print(" \_____|\__,_|\___||___/___/  \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|                (ai)")
    print("")
    print("Think of a number, 1 - 100, and I'll think of it.")
    print("")
    input("Press enter to begin ")
    play()

def play():
    run_game()
    
       
def run_game():

    #tries += 1

    tries = 0
    allotted_tries = 7

    is_game_over = False


    max_num = 100
    min_num = 1

    lower_responses = ["No, lower", "lower", "Lower", "low", "l"]
    higher_responses = ["No, Higher", "higher", "Higer", "high", "h"]
    yes_responses = ["Yes", "yes", "y", "Y"]


    while is_game_over == False:
        guess = (max_num + min_num) // 2

        
        
        ans = input("Is " + str(guess) + " your number? ")
        ans = ans.lower()
        
        if ans in lower_responses or ans in higher_responses or ans in yes_responses: 

            tries += 1

            if ans in yes_responses and tries < allotted_tries:
                print("I Won! It only took me " + str(tries) + " tries!")
                is_game_over = check_restart()

            elif ans in lower_responses and tries < allotted_tries:
                max_num = guess - 1
            elif ans in higher_responses and tries < allotted_tries:
                min_num = guess + 1
                
                
            elif tries == allotted_tries:
                print("game over")
                is_game_over = check_restart()
                
        else:
            print(ans + " not valid.")

def check_restart():

    yes_responses = ["Yes", "yes", "y", "Y"]

    ans = input("Would You Like To Play Again? ")

    if ans in yes_responses:
        return False
    else:
        return True
        
    
                

              

start()
