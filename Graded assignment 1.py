# joining the lists to make one list and then defining list

lst = [[5, 7, 8, 7, "a", "b", "a", 5], [6, 9, 0, 9, 6, 0]]
newlst = [x for l in lst for x in l]
print(newlst)
lstA = (newlst[0:8])
lstB = (newlst[8:14])
print("List A is as follows: " , lstA)
print("List B is as follows: " , lstB)


# checking for duplicates in list

 
def unique(lstA):
     
    list_set = set(lstA)
    unique_list = (list(list_set))
    for x in unique_list:
        print x,
    print("the unique values from 1st list is")
unique(lstA)
 

