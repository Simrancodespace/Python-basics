# A) Basic Array operations using Numpy library
import numpy as np

# Creating NumPy arrays
array1 = np.array([10, 20, 30, 40])
array2 = np.array([50, 60, 70, 80])

# Basic operations
# 1. Addition
addition = array1 + array2
print("Addition:", addition)

# 2. Subtraction
subtraction = array2 - array1
print("Subtraction:", subtraction)

# 3. Multiplication (element-wise)
multiplication = array1 * array2
print("Multiplication:", multiplication)

# 4. Division (element-wise)
division = array2 / array1
print("Division:", division)
print("--------------------------")

# 5. Scalar operations
scalar_multiplication = array1 * 2
print("Scalar Multiplication:", scalar_multiplication)
print("--------------------------")

# 6. Dot product
dot_product = np.dot(array1, array2)
print("Dot Product:", dot_product)
print("--------------------------")

# 7. Array statistics
print("Sum of array1:", np.sum(array1))
print("Mean of array2:", np.mean(array2))
print("Max of array1:", np.max(array1))
print("Min of array2:", np.min(array2))
print("--------------------------")

# 8.reshape
array3 = np.array([12, 24, 36, 48, 60, 72])
reshaped_arr = array3.reshape((2, 3))
print(reshaped_arr)
print("--------------------------")

# Concatenating Arrays
concatenated_arr = np.concatenate((array1, array2), axis=0)
print(concatenated_arr)
print("--------------------------")

# 9.statistical function
mean_value = np.mean(array1)
std_value = np.std(array1)
min_value = np.min(array1)
max_value = np.max(array1)
print(mean_value)
print(std_value)
print(min_value)
print(max_value)
print("--------------------------")

# 10.Boolean Indexing
mask = array1 > 2
print(array1[mask])


# B) Implement User defined Functions
# 1) Program to demonstrate the use of user defined functions
def sum(a, b):
    total = a + b
    return total
x = 50
y = 80
print("The sum of", x, "and", y, "is:", sum(x, y))

# 2)Python code to print factorial of a given number
def recursive_func(num):
    # Base case
    if num == 0:
        return 1
    else:
        # Recursive case
        return num * recursive_func(num - 1)
print(recursive_func(6))


# 3)Fibonacci
def fibonacci_func(num):
    if num <= 1:
        return num
    else:
        return fibonacci_func(num - 1) + fibonacci_func(num - 2)
nterms = int(input("Enter Total terms to be printed: "))
if nterms <= 0:
    print("Invalid input")
else:
    print("Fibonacci numbers are:")
    for i in range(nterms):
        print(fibonacci_func(i), end=" ")


# 4) Variable length argument functions
# function defination
def fun(*args):
    for arg in args:
        print(arg)
# Function calling
fun("Sirman", "Divya", "Sameeksha", "Aditi")

