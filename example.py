import numpy as np

def multiply(a, b):
    return np.dot(a, b)
    
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Result: \n", multiply(a, b))