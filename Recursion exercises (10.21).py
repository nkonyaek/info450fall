""""

# Problem 1 

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


print (f"The GCD of the two numbers is : ",end="")
print (gcd(225,85)) 

"""



"""

# Problem 2 

listA = [-5, 3, 6, 2, -8]

def findMinimum(l):
    if len(l) == 1:
       return l[0]
    
    elif len(l) == 0:
     return print("None")

    else:
       return min(l[0], findMinimum(l[1:]))

findMinimum(listA) 

"""


"""
# Problem 3


def reverseString(s):
    if len(s) <= 1:
        return s
    else:
        return reverseString(s[1:]) + s[0] 


input_string = "python"
reverseString(input_string)


"""

# Problem 4

def palindrome(string):
    if len(string) <=1:
        return True
    elif string[0] != string[-1]:
        return False
    else: 
        reversed(string) == (string)
        return ("Is a palindrome")

palindrome('Kite')