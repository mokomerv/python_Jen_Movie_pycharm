# import statements


# functions go here

# checks that ticket is not blank
def not_blank(question):
    valid = False       # means valid is not true

    while not valid:    # while true
        response = input(question)

        # If name is not blank, program continues
        if response != "":  # if response is not empty
            return response  # return response on line 8

        # If name is blank, show error (& repeat loop)
        else:
            print("Sorry - this can't be blank, "
                  "please enter your name")


# ******** Main Routine ********

# Set up dictionaries/ lists needed to hold data

# Ask user if they have used the program before and show instructions if necessary

# Loop to get ticket details


# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:  # If no. tickets left are less than 4
        print("You have {} seats "
              "left".format(MAX_TICKETS - count))

    # Warns user that only one seat is left! when count (no. tickets left) are 4
    else:
        print("*** There is only ONE set left!! ***")

    # Get details

    # Get name (can't be blank)
    name = not_blank("Name: ")
    count += 1
    print()  # This loop has finished. It will print out from the while loop.

if count == MAX_TICKETS:
    print("You have sold all the tickets!")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still left".format(count, MAX_TICKETS - count))


    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)


    # CalculateTotal sales and profit
