# Corey Verkouteren
# 8/27/2021
# Mr Ball's class
# Practicing using lists/list introduction

# Magic 8Ball program

import random as rdm
myResponses = ["Don't count on it", "If you think so", "Is the sky blue?", "Nope", "Yeah, sure...",
               "It should be obvious", "... ask a different question", "Probably"]
# ^ List of responses
running = True
while running:
    input("Go ahead, ask a question: ")
    BallResponse = rdm.choice(myResponses)
    # ^ picks a random response from "myResponses" list
    print(BallResponse)
    print()
    # ^ prints the response chosen and adds a space in the terminal to see the question below better
    theyinput = input("Would you like to ask another question?(type yes or no): ")
    if theyinput.lower() == "no":
        running = False
    elif theyinput.lower() == "yes":
        continue
    else:
        print("that is not 'yes' or 'no'")
        break
    # ^ either returns to start of loop or ends the program, if the input isn't 'yes' or 'no' it breaks the loop
