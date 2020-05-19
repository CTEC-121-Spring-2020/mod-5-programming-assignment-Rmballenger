# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Robert Ballenger

# IPO

# function definition


def convertNumber(numberGiven):

    # Here a if/elif loop occurs where it checks if the numberGiven is equal to any of the numbers below, and if it does it prints the message.

    if numberGiven == 1:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is I")

    elif numberGiven == 2:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is II")

    elif numberGiven == 3:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is III")

    elif numberGiven == 4:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is IV")

    elif numberGiven == 5:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is V")

    elif numberGiven == 6:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is VI")

    elif numberGiven == 7:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is VII")

    elif numberGiven == 8:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is VIII")

    elif numberGiven == 9:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is IX")

    elif numberGiven == 10:
        print("Your number of", numberGiven,
              "converted to Roman Numerals is X")

    # Here it checks if the number is out of the 1-10 range.

    elif numberGiven > 10 or numberGiven < 1:
        print("I said a number BETWEEN 1 and 10.\nPlease try again...")

    return

    '''
        main()
        '''


# unit test function


def unitTest():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Unit Tests")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Here in my unit testing, I run a loop that checks the function with all all the potentail options the function is set to expect. I decided to use a range of 12 so both 0 and 11 are tested as well.

    for numberGiven in range(12):
        convertNumber(numberGiven)

    print("\n")


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Main")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # For my main function here, it's just a simple input request. I do have an int selected so it makes sure to send the number as an int and not a string. I also added a break for readability. The program then calls the function convertNumber() with the paramater of whatever number was given by the user.

    numberGiven = int(input("Pick a number 1 through 10\n"))
    convertNumber(numberGiven)


unitTest()
main()
