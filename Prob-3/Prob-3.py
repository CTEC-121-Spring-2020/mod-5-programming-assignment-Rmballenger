# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Robert Ballenger

# IPO
# Input - Get the size of the job in square feet, and the price for a gallon of paint.
# Process - All the math garbage. Bleh I hate math.
# Output - Print's a list for the user including: Number of gallons of paint required, Hours of labor required, Cost of the paint, Labor Charges, and Total cost of the job.
#
# Data: 112 Square feet per 1 gallon and 8 hours of labor
#


# Is there a reason to have the main function listed last? I see it frequently but feel it being first makes more sense. Either way, couple of variables being created here from user input. I force it to store them as int and float as I need a whole number for one and a decimal for the other.
# Then I call the next function, sending the variables I've just made over.
def main():
    print("Howdy, thanks for choosing Professional Finger Painting\nThe only painting company that paints truely by 'hand'!")
    squareFootage = int(
        input("To start, please enter how many square feet you need painted: "))
    pricePaint = float(
        input("Great! Next, enter the cost of the paint you want to use: "))

    costEstimate(squareFootage, pricePaint)


# The function that does all the work. Bringing in the variables from before and run the basic math. Detailed comments within to explain my choices.
def costEstimate(squareFootage, pricePaint):

    # For this I need a variable for the number of gallons of paint> I run the sqft variable from before and divide it by 112 which is the wall space per gallon. After, I run a if statement as putting a sqft less than 112 resulted in 0 gallons of paint required.
    gallonsOfPaint = squareFootage / 112
    if gallonsOfPaint < 1:
        gallonsOfPaint = 1

    # Few more variables in the same mannor. Using 8 for the hours per gallon, and 35 for dollars per hour worked. Last a 99 dollar edition for the one time setup fee.
    hoursOfLabor = gallonsOfPaint * 8
    totalPricePaint = gallonsOfPaint * pricePaint
    totalLaborCost = hoursOfLabor * 35
    overallTotalCost = totalPricePaint + totalLaborCost + 99

    # I don't know how to send new variables BACK to the main() function, so I'm creating a new one and sending the variables I have now over to it.
    printReceipt(gallonsOfPaint, hoursOfLabor, totalPricePaint,
                 totalLaborCost, overallTotalCost)


# Last function here of the program, taking the variables from before, I toss in a couple print statements to make it readable for the user.
def printReceipt(gallonsOfPaint, hoursOfLabor, totalPricePaint, totalLaborCost, overallTotalCost):
    print("Sounds great! We can total that up for you here as an itemized receipt!\n")
    print("Gallons of Paint required:", int(gallonsOfPaint))
    print("Hours to complete the job:", hoursOfLabor)
    print("Total price of the paint:", totalPricePaint)
    print("Labor charges:\t\t", totalLaborCost)
    print("One time setup fee: \t 99")
    print("--------------------------------")
    print("Your total cost: \t $", overallTotalCost)


main()
