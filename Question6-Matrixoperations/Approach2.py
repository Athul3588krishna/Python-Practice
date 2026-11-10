import numpy as np

a = np.array(eval(input("Enter first matrix: ")))
b = np.array(eval(input("Enter second matrix: ")))

print("Addition:\n", a+b)
print("Subtraction:\n", a-b)
print("Multiplication:\n", np.dot(a,b))

n = int(input("Enter scalar value: "))
print("Scalar Multiplication:\n", a*n)

print("Transpose:\n", a.T)