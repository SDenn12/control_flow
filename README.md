## Static Methods
```
# create a class which contains functions


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
print(Calculator.add(1, 2))  # returns 3
print(Calculator.subtract(1, 2))  # returns -1
print(Calculator.multiply(1, 2))  # returns 2
print(Calculator.divide(1, 2))  # returns 0.5
```
## Functions
```python
from datetime import date


# Task 1
# Version 1
def version_one():
    name = "Random String"
    name = "sAM   ".lower().capitalize().replace(" ", "")
    last = "DENNIS              ".lower().capitalize().replace(" ", "")
    print(len(name))
    full_name = name + " " + last

    print(f"Welcome {full_name}")


# Version 2
def version_two():
    full_name = "Random String"
    full_name = "sam dennis"
    first, last = full_name.split(" ")
    f_n = first.lower().capitalize()
    l_n = last.lower().capitalize()
    print(f"Welcome {f_n} {l_n}! ")


version_one()
version_two()


# Task 2
def birth_year(name, age, birthday):
    current = date.today().year
    birthday = birthday.split("-")

    if date.today().month > int(birthday[0]):
        birthday_yet = True

    elif date.today().month == int(birthday[0]):
        if date.today().day >= int(birthday[1]):
            birthday_yet = True
        else:
            birthday_yet = False

    elif date.today().month < int(birthday[0]):
        birthday_yet = False

    else:
        print("That was not a valid birthday")


    if birthday_yet:
        birthyear = current-age
    else:
        birthyear = current-age-1

    return f"OMG {name}, you are so old you were born in {birthyear}"

# nm = input("What is your name? ")
# ag = int(input("How old are you? "))
# bday = input("When was your birthday? Format as MM-DD")
# print(birth_year(nm, ag, bday))


# Task 3
def spirit_animal(name, height, fav_col, spir_ani):
    name = name.lower().capitalize()

    print(f"Welcome {name}. \nYou're {height}m tall. \nYour favourite colour is {fav_col}. "
          f"\nYour secret begins with {spir_ani[0]} and ends with {spir_ani[-1]}. "
          f"\nThe length of the word is {len(spir_ani)}")
    guess = input("\nGuess what the spirit animal is! ")

    if spir_ani.lower() == guess.lower():
        return "\nWow how did you know? :DD"
    else:
        return "\nSorry that is incorrect."


# name = input("What is your name? "
# height = input("What is your height? ")
# fav_col = input("What is your favourite colour? ")
# spir_ani = input("What is your spirit animal? ")
# print(spirit_animal(name, height, fav_col, spir_ani))

def hero_story():
    story = {
        "start": "James woke up one morning and went to the shop.",
        "middle": "James got mugged at the shop.",
        "end": "Shop owner called the police. The end."
    }

    print(type(story))
    print(story.keys())
    print(story.values())
    print("\nStory Begins\n ")

    for key in story.keys():
        print(story[key])

    story["hero"] = "Super Pravin turns up saves the day"
    print("\n\n")
    for key in story.keys():
        print(story[key])


# hero_story()

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
