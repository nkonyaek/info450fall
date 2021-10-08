lst = ['Beware the Jabberwock, my son,',  'the jaws that bite, the claws that catch,', 'Beware the JubJub bird and shun', 'the frumious bandersnatch']

# Print text to output file
textfile = 'carroll.txt'
with open(textfile, 'w') as f:
 for element in lst:
    f.write(element + "\n")

# Print length of longest line in file
large_line_len = 0
with open(textfile, 'r') as f:
 for line in textfile:
    if len(line) > large_line_len:
        large_line_len = len(line)


print("The length of the longest line is: " , len(max(open(textfile), key=len)) ,"characters.")
print ("The longest line in the console is as follows: ", max(open(textfile), key=len))