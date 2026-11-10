import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Addition:")
print(a + b)

print("Subtraction:")
print(a - b)

print("Multiplication:")
print(np.dot(a, b))

print("Scalar Multiplication:")
print(a * 2)

print("Transpose:")
print(a.T)