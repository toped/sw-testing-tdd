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
import math

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

def calculateDistance(x1, y1, x2, y2):
    result = None
    
    # ensure x and y values are either a float or int
    if((isinstance(x1, int) or isinstance(x1, float)) and (isinstance(x2, int) or isinstance(x2, float)) and (isinstance(y1, int) or isinstance(y1, float)) and (isinstance(y2, int) or isinstance(y2, float))):
        #ensure x and y values are not larger than 1000000000
        if(x1 > 1000000000 or x2 > 1000000000 or y1 > 1000000000 or y2 > 1000000000):
            result = "One of your values is too large. x and y values must be <= 1000000000."
        #ensure x and y values are not smaller than -1000000000
        elif(x1 < -1000000000 or x2 < -1000000000 or y1 < -1000000000 or y2 < -1000000000):
            result = "One of your values is too small. x and y values must be >= -1000000000."
        #else return resulting distance
        else:
            result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    #else display that x or y value is not numeric
    else:
        result = "One of your values is not numeric. x and y values must be either an integer or float."
       
    # return resulting integer, float, or string
    return result
    

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

