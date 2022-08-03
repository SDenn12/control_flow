```python
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
