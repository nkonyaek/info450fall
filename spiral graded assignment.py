def check_odd():
 n = int(input("Please enter an odd integer: ")
 if n % 2 != 0:
    return n
 else:
    return print("Error! The number you have entered is not odd.")

check_odd()

import numpy as np
def spiral_array(A):
 A = np.array(A)
 out = []
 while(A.size):
     out.append(A[0][::-1])    
     A = A[1:][::-1].T         
 return np.concatenate(out)
