# Homework 09.16.2021 Part 2


str1 = str(input("Please enter a string: "))
num2 = int(input("Please enter an integer: "))

while (len(str1)) % num2 == 0:
    k = 3
    res = [str1[i: j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1) if len(str1[i:j]) == k]
    print("The substrings of your input string is as follows : " + str(res))
   
    break
else: 
        print("The integer is not a factor of the string length. Try again.") 

