input_text = "this is a sample text with several words " 
input_text += "this is a more same text with different words" #Define input

x = input_text.split() # Split words into separate values in a list

input_dict = {} # Create dictionary
for item in x:
    if item not in input_dict:  # Count the number of times each word appears
        input_dict[item] = 1
    else:
        input_dict[item] += 1

print(input_text) # Print original list of words

print("The number of times each word appears is: ")
for word, count in input_dict.items():
    print(f"{word}: {count}") # Output the number of each word
