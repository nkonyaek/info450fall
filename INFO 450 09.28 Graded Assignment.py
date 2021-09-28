# Define empty responses dictionary
responses_dict = {}

# Set a flag to indicate that the user's responses are active.
program_active = True

while program_active:
    # Prompt for the person's state and fact of choice.
    state = input("\nWhat is your state of choice? ")
    fact = input("What is a fact about that state? ")
    # Store the state in the dictionary.
    responses_dict[state] = fact
    # Find out if the user wants to add any more states or facts.
    repeat = input("Would you like to add another state and fact? Type q if you wish to stop. (yes or q) ")
    if repeat == 'q':
       program_active = False
       
# Print back the states and facts.
print("\n--- State & Facts Questionnaire Results ---")
for state, fact in responses_dict.items():
       print(f"A fact about the state of {state} is {fact}.")
