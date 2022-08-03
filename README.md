## Functions
```
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
```

## Conditions

```
python
# if, elif, else


# learn loops (for/while)
# dont have to repeat yourself
# help with iteration

shopping_list = ["fruits", "milk", "bread", "cream"]
print(shopping_list)
for item in shopping_list:
    print(item)
    if item == "bread":
        break

dictionary = {
    'name': 'Sam',
    'age': 21,
    'salary': 10,
    'address': 'AA11AA',
    'spir_ani': 'panda',
    'fav_col': 'red'
}

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key in dictionary.keys():
    print(f"{key} - {dictionary[key]}")

# print("\n")
# i = 0
# while i < len(shopping_list):
#     print(shopping_list[i])
#     i += 1

```
