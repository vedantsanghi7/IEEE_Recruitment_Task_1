import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))
print("Original 5x5 Matrix:")
print(matrix)

middle_matrix = matrix[1:4, 1:4]
print("\nMiddle 3x3 Matrix:")
print(middle_matrix)

first_row = middle_matrix[0, :]
last_column = middle_matrix[:, -1]
dot_product = np.dot(first_row, last_column)
print(f"\nDot product of the first row and last column: {dot_product}")

