# Start a loop that will run until the user enters 'q' for quit.

state = input ("Enter a state or type q to quit: ")
while state != 'q':
        # Ask the user for their state of choice.

    facts = input ("Enter a fact about the state or type q to quit: ")
    if facts != 'q': 
        new_state = input ("Enter a new state or type q to quit: ")
else:

    print ("You have decided to quit the program. Goodbye!")
