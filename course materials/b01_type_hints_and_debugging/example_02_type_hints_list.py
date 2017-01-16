# Specify the type of element held in a list using list[int]
# Note, this does work with list rather than typing.List
# but best practice to use typing.List, as it also allows
# you to define the type of element held in the list


from typing import List


def print_list(my_list: List):
    for my_element in my_list:
        print(my_element)

print_list(['a', 'b', 'c'])
print_list([1, 2, 3])

print_list(1)

