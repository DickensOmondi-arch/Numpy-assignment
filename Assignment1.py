import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

add_result = A + B
print("\nElementwise Addition (A + B):")
print(add_result)

mul_result = A * B
print("\nElementwise Multiplication (A * B):")
print(mul_result)

matmul_result = A @ B
print("\nMatrix Product (A @ B):")
print(matmul_result)
