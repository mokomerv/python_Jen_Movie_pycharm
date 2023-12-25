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

    # Get name (can't be blank)
    
name = not_blank("Name: ")
    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)


    # CalculateTotal sales and profit
