# Functions go here


def not_blank(question):
    valid = False       # means valid is not true

    while not valid:    # while true
        response = input(question)

        if response != "":  # if response is not empty
            return response  # return response on line 8
        else:
            print("Sorry - this can't be blank, "
                  "please enter your name")


# Main Routine goes here
name = not_blank("Name: ")