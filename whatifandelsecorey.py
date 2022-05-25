# Corey Verkouteren
# 8/26/2021
# Mr. Ball's class
# Using if and else statements

# This program checks if a number is between 10 and 25
Answer = input("Please input a number between 10 and 25: ")
theynum = int(Answer)
# ^ Takes input from user and converts to an integer for comparison
if theynum < 10:
    print("Try again, your number was less than 10")
elif theynum > 25:
    print("Try again, Your number was more than 25")
# ^ these 2 if/elif statements check if the number is less than 10 or more than 25
else:
    print("Thank you,", theynum, "is between 10 and 25")
# ^ Thanks user if the number doesn't fall into the if or elif statement above (meaning it is between 10 and 25)
