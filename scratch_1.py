import numpy as np
import time

# Exercise 1: Why is NumPy Faster?
print("Exercise 1:")
size = 1_000_000
list_numbers = list(range(size))
numpy_numbers = np.arange(size)

# Time squaring using Python lists
start_time = time.time()
list_squared = [x**2 for x in list_numbers]
list_time = time.time() - start_time

# Time squaring using NumPy arrays
start_time = time.time()
numpy_squared = numpy_numbers ** 2
numpy_time = time.time() - start_time

print(f"Time taken using Python list: {list_time:.5f} seconds")
print(f"Time taken using NumPy arrays: {numpy_time:.5f} seconds")
print()
#results:
#Time taken using Python list: 0.03254 seconds
#Time taken using NumPy arrays: 0.00208 seconds

#Numpy is faster than python lists because Numpy doesn't have to
#chase after pointers and numpy is specifically for numerical data
#and is more efficient and faster when using that data than lists.

# Exercise 2: Create Different Arrays
print("Exercise 2:")
random_matrix = np.random.rand(4, 4)

print("4x4 Matrix of random numbers:")
print(random_matrix)
print("Shape:", random_matrix.shape)
print("Size:", random_matrix.size)
print("Dimensions:", random_matrix.ndim)
print()

# Exercise 3: Random Data Generation
print("Exercise 3:")
# Create a 3x3 identity matrix
identity_matrix = np.identity(3)
print("3x3 Identity Matrix:")
print(identity_matrix)

# Create a 1D array of 20 random integers between 1 and 100
random_integers = np.random.randint(1, 101, size=20)  # Upper bound is exclusive
print("\n1D Array of 20 Random Integers (1-100):")
print(random_integers)
print()

# Exercise 4: Array Slicing
print("Exercise 4:")
# Create a 5x5 matrix of numbers from 1 to 25
matrix_5x5 = np.arange(1, 26).reshape(5, 5)
print("Original 5x5 matrix:")
print(matrix_5x5)

third_row = matrix_5x5[2, :]
print("Third row:")
print(third_row)

last_two_columns = matrix_5x5[:, -2:]
print("Last two columns:")
print(last_two_columns)

center_submatrix = matrix_5x5[1:4, 1:4]
print("3x3 submatrix from the center:")
print(center_submatrix)
print()

# Exercise 5: Reshaping Practice
print("Exercise 5:")
# Create a 1D array of 20 elements
array_1d = np.arange(20)
print("Original 1D array:")
print(array_1d)

# Reshape the 1D array into a 4x5 matrix
reshaped_matrix = array_1d.reshape(4, 5)
print("\n1D array reshaped into a 4x5 matrix:")
print(reshaped_matrix)
