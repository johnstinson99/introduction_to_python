# Specify the type of element held in a list using list[int]
from typing import List


def print_list(my_list: List[int]):
    for my_element in my_list:
        print(my_element + 1)

print_list(['a', 'b', 'c'])

# print_list(1)

# print_list([1, 2, 3])
