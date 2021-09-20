#input given in assignment instructions
#defining lists of lists

student_list= [['Harry', 37.31], ['Barry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39], ["Mike", 27], ["Ella", 90]]

# use sort_key method to set names as key
# use sort method to return a list of the second element in ascending order

def sort_key(name):
    return name[1]
student_list.sort(key=sort_key, reverse=False)

#loop through all the lists and print in scoreboard format

l = ["Name", "   Score"]
print (*l)
for i,j in student_list:
  print(f"{i}\t{j}")


