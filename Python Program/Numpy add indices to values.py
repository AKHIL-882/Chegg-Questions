# importing numpy
import numpy as np
# getting the range of A1[1-100] elements
A1 = np.arange(1,101)
# adding 5 values of index 50 - 55
A2 = A1[50:55]+5
# adding the modified list to the original list
A1[50:55] = A2
# displaying the result
print(A1)