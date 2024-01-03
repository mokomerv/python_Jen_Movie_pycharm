# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    print("You have {} seats "
          "left".format(MAX_TICKETS - count))

    # Get details
    name = input("What is your name?:  ")
    count += 1
    print()  # This loop has finished so it will print out from the while loop.

if count == MAX_TICKETS:
    print("You have sold all the tickets!")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still left".format(count, MAX_TICKETS - count))
