# Define empty dictionary for user's responses
responses_dict = {}

# Set a flag to indicate that the user's responses are active.
program_active = True

while program_active:
 # Create an empty list to add in all facts entered by user and prompt to enter state/facts.
 
 facts = []
 state = input("\nWhat is your state of choice? Enter state or type q to quit: ")

 # If the user decides to quit, it breaks out of the loop and prints the entered inputs. 
 # If not, they may continue entering as many facts/states as they want.

 if state == 'q':
       break
 else:
        entering_facts = True

        while entering_facts:
              new_fact = input("What is a fact about that state? Enter fact or type q to quit: ")
              if new_fact != 'q':
                     facts.append(new_fact)
              else:
                     entering_facts = False

        # Program checks to see if any facts are entered. If the list of facts is not empty, they are stored in the dictionary.
        if len(facts) > 0:                          
              responses_dict[state] = facts

        # Prompts if user wants to add any more states or facts.
        repeat = input("Would you like to add another state or fact? Type y to continue. Type q for quit if you wish to stop: ")
        if repeat == 'q':
              program_active = False


# The loop has ended. Print back the states and facts.
print("\n--- State & Facts Questionnaire Results ---")
for state, fact in responses_dict.items():
       print(f"Fact(s) about the state of {state} are:")
       print(*fact, sep = "\n")
