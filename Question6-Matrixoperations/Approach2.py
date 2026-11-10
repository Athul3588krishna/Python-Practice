import numpy as np

a = np.array(eval(input("Enter first matrix: ")))
b = np.array(eval(input("Enter second matrix: ")))

print("Addition:\n", a+b)
print("Subtraction:\n", a-b)
print("Multiplication:\n", np.dot(a,b))

n = int(input("Enter scalar value: "))
print("Scalar Multiplication:\n", a*n)

print("Transpose:\n", a.T)

### Algorithm – Matrix Operations Using NumPy

1. Start.
2. Import the NumPy library.
3. Read two matrices from the user.
4. Convert the input matrices into NumPy arrays.
5. Perform matrix addition and display the result.
6. Perform matrix subtraction and display the result.
7. Perform matrix multiplication using `np.dot()` and display the result.
8. Read a scalar value from the user.
9. Perform scalar multiplication and display the result.
10. Find the transpose of the first matrix and display the result.
11. Stop.