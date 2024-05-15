import numpy as np

# Create a 1-dimensional array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1d)
print()

# Create a 2-dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr2d)
print()

# Array Attributes
print("Array Attributes:")
print("Shape:", arr2d.shape)
print("Data Type:", arr2d.dtype)
print("Number of Dimensions:", arr2d.ndim)
print("Size (Total Number of Elements):", arr2d.size)
print()

# Array Indexing and Slicing
print("Array Indexing and Slicing:")
print("Element at row 1, column 2:", arr2d[1, 2])
print("First row:", arr2d[0])
print("Last column:", arr2d[:, -1])
print()

# Array Operations
print("Array Operations:")
print("Sum of all elements:", np.sum(arr2d))
print("Mean of each row:", np.mean(arr2d, axis=1))
print("Maximum element:", np.max(arr2d))
print()

# Reshaping Arrays
print("Reshaping Arrays:")
arr1d_reshaped = arr1d.reshape(5, 1)
print("1D Array Reshaped:")
print(arr1d_reshaped)
print()

# Array Broadcasting
print("Array Broadcasting:")
arr_broadcasted = arr1d + 10
print("Broadcasted Array:")
print(arr_broadcasted)
