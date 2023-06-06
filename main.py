# Variables and Data Types:
# integers, floats, strings, booleans, and lists.

name: str = "John"
age: int = 25
height: float = 1.75
is_student: bool = True
#
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))




# # Control Flow:
# #   Use if-else statements for conditional branching.
# #   Use loops (such as for and while) for repetitive tasks.
#
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

for i in range(1, 5):
    print(i)

condition = True

# while condition:# code block
#     print(f'this is the condition: {condition}')
#
#
# Functions:
#     Functions are reusable blocks of code that perform specific tasks.
#     They help organize your code and make it more modular.

def cumprimento(name):
    print(f"Buenas, {name}!")

cumprimento("Carlos")

#
# # Libraries and Modules:
# import math
#
# result = math.sqrt(25)
# print(result)
#
#
# # Error Handling (try-except):
#
# try:
#     # Code that may raise an exception
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except Exception as e:
#     print("An error occurred:", str(e))
#
#
# # File Handling (reading and writing files):
#
# # Reading from a file
# try:
#     with open("myfile.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")
#
# # Writing to a file
# try:
#     with open("myfile.txt", "w") as file:
#         file.write("Hello, world!")
#         print("File written successfully.")
# except Exception as e:
#     print("An error occurred:", str(e))
