# The chosen text is "The Secret of Shangore; by Nicholas Carter"

# This is a program to read how many times "the" and "follow" appear in the mentioned text.
def count_file():
 try:
  filename='book.txt'
  with open('book.txt',encoding='utf-8') as f:
   contents=f.read()     
 except FileNotFoundError:
  print(f"Sorry, the file {filename} does not exist.")
 else:
    words = contents.lower().count('the')
    print(f"The word 'the' in the book 'The Secret of Shangore by Nicholas Carter appears' about {words} times.")

    words2 = contents.lower().count('follow')
    print(f"The word 'follow' in the book 'The Secret of Shangore by Nicholas Carter appears' appears about {words2} times.")

count_file()

# Writing the output to a new file.
# filename = 'bookwordcount.txt'
# with open(filename, 'w') as f:
# f.write()