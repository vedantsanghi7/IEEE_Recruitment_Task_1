import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))
print("Original 5x5 Matrix:")
print(matrix)

print(f"\nMaximum: {matrix.max()}")
print(f"Minimum: {matrix.min()}")
print(f"Mean: {matrix.mean()}")

# Normalizing the matrix to a 0-1 scale using its deviation from the minimum
normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
flattened_array = normalized_matrix.flatten()
sorted_array = np.sort(flattened_array)

print("\nUpdated Array:")
print(sorted_array)