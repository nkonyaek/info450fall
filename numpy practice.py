import numpy as np


array1 = np.ones((5,5)) # create a 5x5 array of all ones


array2 = np.arange(2,51,2) # creates array of even numbers from 2 to 20, inclusive

array3 = np.full((13, 13), 13) # creates a 13x13 array where every value is equal to 13


array4 = np.arange(1,26) # creates array of 1 to 25, inclusive
a = array4.reshape(5,5)  # arranges into a 5x5
print(a)

b = array4.ravel()  # creates a 1D view
print(b)