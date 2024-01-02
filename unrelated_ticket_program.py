# Write an application to pre-sell a limited number of cinema tickets. Each buyer can buy as many as 4 tickets.
# No more than 100 tickets can be sold. Implement a program called TicketSeller that prompts the user for
# the desired number of tickets and then displays the number of remaining tickets. Repeat until all tickets
# have been sold, and then display the total number of buyers.

ticketsRemaining = 100  # Set variable for remaining tickets to 100 as starting counter outside of the loop
ticketCounter = 0  # Setting the counter variable to 0 to start

while True:

    # ticketCounter= 0 #Setting the counter variable to 0 to start

    TicketSeller = float(input('Please enter the number of tickets you would like to purchase: '))

    if TicketSeller <= 4:  # If TicketSeller input is less than or equal to 4
        print("You've purchased", int(TicketSeller), 'tickets!')  # Print if true
        ticketCounter = ticketCounter + 1  # Start counter
        ticketsRemaining = int(ticketsRemaining - TicketSeller)  #
    else:
        print('The maximum amount of tickets you can buy is 4.')  # TicketSeller variable is >4, prompt

    print(ticketCounter, "total ticket(s) have been purchased!")  # Print counter and add 1 for first ticket purchase
    print(ticketsRemaining, "ticket(s) remaining!")
    # if ticketCounter <= 100