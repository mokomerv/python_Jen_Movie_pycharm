# Functions go here


def not_blank(question):
    valid =input("Please enter your name?:")

    while not valid:
        response = print("Sorry - this can't be blank, please enter your name?:")

        if response != valid:
            print("dumass")

        else:
            print("Chur")



# Main Routine goes here
name = not_blank("Name: ")