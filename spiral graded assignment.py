import numpy as np

def spiral_array(n):
 A = np.zeros(shape=(n,n))
 center = (n - 1) / 2
 row = center
 column = center
 print(A)
 


 #while(A.size):
    # out.append(A[0][::-1])    
    # A = A[1:][::-1].T         
 #return np.concatenate(out)

n = int(input("Please enter an odd integer: "))
if n % 2 != 0:
       spiral_array(n)
else:
    print("The number you have entered is not odd. Please try again.")
