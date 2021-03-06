import numpy as np
    
def spiral_array(n):
 A = np.zeros(shape=(n,n), dtype=int)
 center = int((n - 1) / 2)
 
 row_start = center
 row_end = center + 1
 
 col_start = center
 col_end = center + 1
 
 current = 1
 
 A[row_start][col_start] = current
 current += 1
 while True:
     # base case
    if current > n * n:
        break
     
    # go right
    for i in range(col_start + 1, col_end + 1):
        if current > n * n:
            break
        A[row_start][i] = current
        current += 1
    col_start-= 1
    
    # go down
    for i in range(row_start + 1, row_end + 1):
        if current > n * n:
            break
        A[i][col_end] = current
        current += 1
    row_start -= 1

    # go left
    for i in range(col_end - 1, col_start - 1, -1):
        if current > n * n:
            break
        A[row_end][i] = current
        current += 1
    col_end += 1
    
    # go up
    for i in range(row_end-1, row_start - 1, -1):
        if current > n * n:
            break
        A[i][col_start] = current
        current += 1
    row_end += 1
 return A

n = int(input("Please enter an odd integer: "))
if n % 2 != 0:
       print(spiral_array(n))
else:
    print("The number you have entered is not odd. Please try again.")
