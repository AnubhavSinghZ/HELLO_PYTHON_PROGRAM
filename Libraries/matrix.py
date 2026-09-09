import numpy as np  # Import the NumPy library

# 1. Create a 1D array (a simple list of numbers)
a1 = np.array([1, 2, 3, 4, 5])
print("Original 1D Array:", a1)

# 2. Add 2 to every element instantly (no loops needed!)
print("Add 2 to each element:", a1 + 2)

# 3. Create a 2D array (a matrix with 2 rows and 3 columns)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Matrix:\n", matrix)

# 4. Get the shape (rows, columns) of the matrix
print("Shape of matrix:", matrix.shape)

# 5. Find the sum of all numbers in the matrix
print("Total sum:", matrix.sum())
