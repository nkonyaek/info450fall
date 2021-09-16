#Homework 09.16.2021 part 1

num = int(input("Please enter a prime number less than 100: "))
if num > 1 and num <101: 
    for i in range(2,num):
       if (num % i) == 0:
           print(num,"is either not a prime number or not within range.")
           print("It is not a prime number because", i,"times",num//i,"is",num)
           break
    else:
       print(num,"is a prime number. The list of prime numbers up until", num, "are as follows: ")
       n = num
       for i in range (2,n+1):
           if i>1:
            for j in range (2,i):
                if (i%j) == 0:
                    break
            else:
                print(i)
else:
   print(num,"is not a prime number or not within range. Program terminated.")
   


