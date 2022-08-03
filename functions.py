# What is a function
# Why do we need it -
# DRY Do Not Repeat Yourself
# Syntax def function_name():

# first iteration
# def greet_user():
#     print("welcome user")


# greet the user with their name
# prompt the user to enter their name
def greet_user(name):
    print(f"Welcome {name}")


greet_user("Sam")


# create a function that takes two arguments


class Calculator:
    # creates add method
    # declares static method (unrelated to the class object itself, convenient for storing related methods)
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    # creates subtract method
    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    # creates multiply method
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    # creates divide method
    @staticmethod
    def divide(num1, num2):
        return num1 / num2


# prints the functions
print(Calculator.add(1, 2))
print(Calculator.subtract(1, 2))
print(Calculator.multiply(1, 2))
print(Calculator.divide(1, 2))
