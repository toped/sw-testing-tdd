"""
Assignment 4: Test Driven Development and Unit Testing

Objective:
Use test driven development to implement a set of software requirements. Write unit tests to provide full
coverage of developed code base using multi faceted independent tests. Create a control flow graph. Groups up
to 6.

Authors:
Tope Daramola
Hannah Church
Dylan Jaye
Mauri Mitchell

Python v2.7

"""


# This function prints the user menu
def printMenu():
    print ("""
        1. Calculate Body Mass Index
        2. Find out if I can meet my savings goal
        3. Find the distance between two points
        4. Verify if my email address is valid
        """)


def calculateBMI(heightFeet, heightInches, weight):
    print("\n TO-DO: complete function")

def calculateRetirement(age, salary, percentSaved, savingsGoal):
    print("\n TO-DO: complete function")

def calculateDistance(x1, y1, x2,y2):
    print("\n TO-DO: complete function")

def verifyEmailAddress(inputEmail):
    print("\n TO-DO: complete function")


#Print the Menu
printMenu()

#Prompt user for the function that they want to run
funcType = '1' #input("What would you like to calculate? ")

if funcType == "1":
    print("\n BMI Calculator")
    print("\n TO-DO: prompt for user input then call function to return output")
elif funcType == "2":
    print("\n Savings Goal Calculator")
    print("\n TO-DO: prompt for user input then call function to return output")
elif funcType == "3":
    print("\n Distance Calculator")
    print("\n TO-DO: prompt for user input then call function to return output")
elif funcType == "4":
    print("\n Email Verifier")
    print("\n TO-DO: prompt for user input then call function to return output")

