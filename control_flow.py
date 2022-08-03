# if, elif, else


# learn loops (for/while)
# dont have to repeat yourself
# help with iteration

# shopping_list = ["fruits", "milk", "bread", "cream"]
# print(shopping_list)
# for item in shopping_list:
#     print(item)
#     if item == "bread":
#         break
#
# dictionary = {
#     'name': 'Sam',
#     'age': 21,
#     'salary': 10,
#     'address': 'AA11AA',
#     'spir_ani': 'panda',
#     'fav_col': 'red'
# }
#
# # creates a variable called keys and assigns the value of dictionary.keys() to it
# for key in dictionary.keys():
#     print(key)
#
# # creates a variable called value and assigns the value of dictionary.values() to it
# for value in dictionary.values():
#     print(value)
#
# # creates a variable called keys and assigns the value of dictionary.keys() to it for each iteration
# for key in dictionary.keys():
#     print(f"{key} - {dictionary[key]}")  # presents the key and value in a string

# use case of multiple conditions
# create a list with int values 1-4
# iterate through the list using for loop

# for i in range(1, 5):
#     if i == 3:
#         print("found", 3)
#     elif i > 3:
#         print("gone too far")
#     else:
#         print("too soon")

# While loops
# mainly used in monitoring a situation
# print the number with message stating its working

# i = 0
# # iterates while number is less than 10
# while i < 10:
#     print(f"its working {i}")
#     i += 1  # adds 1 to each iteration
#

user_prompt = True
while user_prompt:
    age = input("Please enter your age. ")
    if age.isdigit():
        if int(age) > 177:
            print("That is too old. ")
        else:
            user_prompt = False
    else:
        print("Please enter numbers only")


# print a message stating your age is whatever the input user entered
print(f"your age is {age}")

# using the above use case also check if the user age is less than 117 years before you