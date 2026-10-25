# Basic data types

a = 27
b = 09.3
name = "Simran"
status = True
print("type of a",a, type(a))
print("type of b",b, type(b))
print("String:", name, type(name))
print("Boolean:", status, type(status))

# Arithmetic Operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("addition: ",a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a **b)

# Relational Operators

a = 178
b = 145
print("a > b:", not(a > b))
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Expressions

a = 7
b = 10
c = 12
result1 = a + b * c
result2 = (a + b) * c
result3 = a / b + c
result4 = a ** c
print("a + b * c =", result1)
print("(a + b) * c =", result2)
print("a / b + c =", result3)
print("a ** c =", result4)

# Conditional statements
# 1.If condition

num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")

# 2.If else condition

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Student has passed")
else:
    print("Student has failed")


# 3. if...elif...else condition

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

# 4.Nested if condition

age = int(input("Enter your age: "))
has_learning_license = input("Do you have learning license? yes/no: ")

if age >= 18:
    if has_learning_license == "yes":
        print("You are eligible to apply for driving license")
    else:
        print("First apply for learning license")
else:
    print("You are not eligible because your age is below 18")

# While Loop

i = 1

while i <= 5:
    print(i)
    i = i + 1

# For Loop

for i in range(1, 6):
    print(i)


# Nested Loop

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Decorators

def login_required(func):
    def wrapper():
        print("Checking login status...")
        func()
        print("User access completed")
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")
dashboard()

# Iterator

name = "SIMRANSINGH"
iterator_obj = iter(name)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

# Generators

def natural_numbers(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter value of n: "))
for num in natural_numbers(n):
    print(num)
