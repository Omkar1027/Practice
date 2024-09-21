import numpy as np

# Create a square matrix
matrix = np.array([[4, 7],
                   [2, 6]])

# Inversion
inv_matrix = np.linalg.inv(matrix)
print("Original Matrix:\n", matrix)
print("Inverse Matrix:\n", inv_matrix)