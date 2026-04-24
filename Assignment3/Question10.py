#Q10. Data Transformation for Model Input (NumPy)

#Context: ML models require structured numeric arrays.

#Tasks:

#1. Create two arrays of shape (3,2)
import numpy as np

array1 = np.array([[1, 2], [3, 4], [5, 6]])
array2 = np.array([[7, 8], [9, 10], [11, 12]])

#2. Perform:
#Vertical stacking
print(np.vstack((array1, array2)))

#Horizontal stacking
print(np.hstack((array1, array2)))

#3. Reshape into (2,6)
reshaped = np.vstack((array1, array2)).reshape((2, 6))
print(reshaped)

#4. Explain:
#Why reshaping is required in ML pipelines