# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Robert Ballenger

# IPO
# Input: Total cost of the transaction and the Amount Tendered
# Process: Subtract cost from tendered, get change amount, and calculate the denominations
# Output: Cost, Tendered, Change, and display the denominations listed out.


# Here at the start of our program, we have a main function that assigns two variables with
# the user input and assigns them both as float. Then I send the variables to a new function.
def main():

    costOfItem = float(input("What was the cost of the item? "))
    amountPaid = float(input("How much did the customer pay? "))

    changeDue(costOfItem, amountPaid)

# In this new function, I draw the two variables from before. More details in comments within.


def changeDue(costOfItem, amountPaid):

    # To start, I assign some variables. I did this originally to make it less confusing but in truth maybe the raw numbers would have worked just the same.
    hundred = 100
    fifty = 50
    twenty = 20
    ten = 10
    five = 5
    one = 1
    quarter = .25
    dime = .10
    nickel = .05
    penny = .01

    # Next we find out the total in change being returned.
    totalDue = amountPaid - costOfItem

    # Now we begin the long run of going down one by one, dividing the total due by the denomination were looking at.
    # Then I create a new 'total' by subtracting whatever might have been removed in finding the amount of denomination used.
    hundredsReturened = totalDue / hundred
    minusHundreds = totalDue - (int(hundredsReturened) * hundred)

    fiftiesReturned = minusHundreds / fifty
    minusFifties = minusHundreds - (int(fiftiesReturned) * fifty)

    twentysReturned = minusFifties / twenty
    minusTwentys = minusFifties - (int(twentysReturned) * twenty)

    tensReturned = minusTwentys / ten
    minusTens = minusTwentys - (int(tensReturned) * ten)

    fivesReturned = minusTens / five
    minusFives = minusTens - (int(fivesReturned) * five)

    onesReturned = minusFives / one
    minusOnes = minusFives - (int(onesReturned) * one)

    quartersReturned = minusOnes / quarter
    minusQuarters = minusOnes - (int(quartersReturned) * quarter)

    dimesReturned = minusQuarters / dime
    minusDimes = minusQuarters - (int(dimesReturned) * dime)

    nickelsReturned = minusDimes / nickel
    minusNickels = minusDimes - (int(nickelsReturned) * nickel)

    penniesReturned = minusNickels / penny

    # Last we create a new function which a WHOLE BUNCH of variables passed with it.
    outputFunction(costOfItem, amountPaid, totalDue, int(hundredsReturened), int(fiftiesReturned), int(twentysReturned), int(tensReturned), int(fivesReturned),
                   int(onesReturned), int(quartersReturned), int(dimesReturned), int(nickelsReturned), int(penniesReturned))


# Into that function, we issue a print statement and go through a if/else loop to list what change is being returned as we don't need to see 0 tens if there's no tens. (Unless that's what you wanted in which case I'd just remove the if/else setup and it would issue the 0's too.)
def outputFunction(costOfItem, amountPaid, totalDue, hundredsReturened, fiftiesReturned, twentysReturned, tensReturned, fivesReturned, onesReturned, quartersReturned, dimesReturned, nickelsReturned, penniesReturned):
    print("Cost: $", costOfItem, "\tTendered: $",
          amountPaid, "\tChange: $", "%.2f" % totalDue)

    if hundredsReturened > 0:
        print(hundredsReturened, " hundreds")
    else:
        pass

    if fiftiesReturned > 0:
        print(fiftiesReturned, " fifties")
    else:
        pass

    if twentysReturned > 0:
        print(twentysReturned, " twenties")
    else:
        pass

    if tensReturned > 0:
        print(tensReturned, " tens")
    else:
        pass

    if fivesReturned > 0:
        print(fivesReturned, " fives")
    else:
        pass

    if onesReturned > 0:
        print(onesReturned, " ones")
    else:
        pass

    if quartersReturned > 0:
        print(quartersReturned, " quarters")
    else:
        pass

    if dimesReturned > 0:
        print(dimesReturned, " dimes")
    else:
        pass

    if nickelsReturned > 0:
        print(nickelsReturned, " nickels")
    else:
        pass

    if penniesReturned > 0:
        print(penniesReturned, " pennies")
    else:
        pass


main()
