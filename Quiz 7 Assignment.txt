# Opens file and reads as list of strings
try:
  filename='accounts_rec.txt'
  with open('accounts_rec.txt') as f:
   contents=f.read()

   # If the file does not exist, python prints out error message   
except FileNotFoundError:
  print(f"Sorry, the file {filename} does not exist.")
else:
 with open(filename) as file:
    string_list = file.readlines()
 
 # Edits the selected strings in list with changes
 string_list[2] = "300 Williamson 0.00\n"
 string_list[3] = "400 Stone -242.16\n"

 # Creating a new file with changes made to original file 
 my_file = open("updated_account_rec.txt", "w")
 new_file_contents = "".join(string_list)
 my_file.write(new_file_contents)
 my_file.close()

 # Printing changes made in python
 readable_file = open("updated_account_rec.txt")
 read_file = readable_file.read()
 print(read_file)
