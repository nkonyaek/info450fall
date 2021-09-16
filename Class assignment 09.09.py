
# Problem 1

a = [(2,5), (1,2), (4,4), (2,3), (2,1)]
a.sort(reverse=True)
print(a)



# Problem 2

list1 = []     
for i in range(1,31):
    list1.append(i ** 2)
print(list1[:6])

# Problem 3

list2 = ["M", "na", "i", "Mi"]
list3 = ["y", "me", "s", "ke"]
list4 = [i + j for i, j in zip(list2, list3)]

output_string = ""
for word in list4:
    output_string += word
    output_string += " "

print(output_string)


# Assignment 1

input_list = ["Mike", 60], ["Joe", 75], ["Sue", 85], ["Anne", 80], ["George", 75]

print("The second lowest score is: ", (sorted(input_list)[2]))

#Assignment 2

input_list = [0, 1, 2, 3]
input_string = "3 2 1 0"
input_tuple = (0, 1, 2, 3)
