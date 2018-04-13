#Thias Kjaer
#Assignment 5
#The program is a high-low guessing game, which generates a random number between 0 and 100, which the user then tries to guess,
#getting information whether the number is higher or lower than their guess.

import random

#setting up variables.
#run is a boolean controlling the first while loop with the main game in it,
#which is false when the user decides to quit
#guesses increments after every guess
#num is the number the user is trying to guess, generated randomly between 0 and 100
run=True
guesses=0
num=random.randint(0,100)
print("Welcome to the Guessing Game!")

while run:
    try:
        guess=input("please enter a number (integer) between 0-100 or quit to give up: ")
        #The else-if block checks the user input to the number or quit in lowercase
        if(guess.lower() == 'quit'):
            print("The number was: %i" %(num))
            run=False
        elif int(guess) < 0:
            print("The range is between 0 and 100")
            guesses += 1
        elif int(guess) > 100:
            print("The range is between 0 and 100")
            guesses+=1
        elif int(guess) > num:
            print("Your guess was too high, try again")
            guesses+=1
        elif int(guess) < num:
            print("Your guess was too low, try again")
            guesses+=1
        else:
            #if everything before fails, the guess must be correct
            guesses+=1
            print("You were right! the number was: %i, you guessed %i times" %(num, guesses))
            #a new while loop is run to allow the user to restart the game
            runagain=True
            while runagain:
                replay=input("To play again type again, to quit type quit: ")
                #if the user decides to restart, a new random number is generated and guesses is reset
                if(replay.lower() == 'again'):
                    num=random.randint(0,100)
                    guesses=0
                    #exiting out of the nested while loop to the main game
                    runagain=False
                #if the user decides to quit, both while loops are exited
                elif replay.lower() == 'quit':
                    runagain=False
                    run=False
                else:
                    print("Please enter only valid input in the form of again or quit")

    except ValueError:
        print("Please enter only valid input in the form of an integer or quit")

print('Thanks for playing')