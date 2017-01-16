import collections
# for my_int in range()
# for my_char in my_string
# for my_int in my_list
# int(string)
# list comprehension, converting each item
# list comprehension, cubing each item.


# basic case for all 3 digit numbers
# for possible_armstrong_number in range(100, 1000):
#     my_digit_list = [int(digit_string) for digit_string in str(possible_armstrong_number)]
#     digits_cubed_list = [my_digit**3 for my_digit in my_digit_list]
#     sum_of_digits_cubed = sum(digits_cubed_list)
#     if sum_of_digits_cubed == possible_armstrong_number:
#         print(possible_armstrong_number)

# Initial Case - no optimisations.
# now extend to generic case
# for power in range(1, 9):
#     print(power)
#     start_of_range = 10**(power-1)
#     end_of_range = 10**(power)
#     # print(start_of_range, end_of_range-1)
#     for possible_armstrong_number in range(start_of_range, end_of_range):
#         my_digit_list = [int(digit_string) for digit_string in str(possible_armstrong_number)]
#         digits_cubed_list = [my_digit ** power for my_digit in my_digit_list]
#         sum_of_digits_cubed = sum(digits_cubed_list)
#         if sum_of_digits_cubed == possible_armstrong_number:
#             print(possible_armstrong_number, sum_of_digits_cubed)

import itertools

# Final optimisation is to reduce the number of powers we have to calculate, eg
# instead of calculating 5^3 + 5^3 + 5^3, calculate 3*5^3
def calc_sum_of_powers(number_list, no_of_digits):
    my_counter = collections.Counter(number_list)
    my_sum = sum([my_counter[my_digit_string] * int(my_digit_string) ** no_of_digits
                  for my_digit_string in my_counter.keys()])
    return my_sum

# First optimisation. Instead of calculating for every number,
# find unique combinations of digits.
# This significantly reduces the number of numbers we need to calculate for.
# If the count of digits of the result matches the count of digits in the number itself,
# then the result is an Armstrong number.
no_of_digits = 3
for no_of_digits in range(3, 20):
    print(no_of_digits)
    digit_combinations_list = itertools.combinations_with_replacement(range(0, 10), no_of_digits)
    # print(list(digit_combinations)[:50])
    # print(len(list(digit_combinations)))
    for a_combination in digit_combinations_list:
        # easier but slower? method, raising each number to a power individually
        # sum_of_cubes_string = str(sum(digit ** no_of_digits for digit in a_combination))
        # calc_sum_of_powers() function looks for duplicates and raises to power once.
        # it returns an integer, so need to convert it to string to find number of digits.
        sum_of_cubes_string = str(calc_sum_of_powers(a_combination, no_of_digits))
        if len(sum_of_cubes_string) == no_of_digits:  # early filtering to reject some
            # convert string back to integers
            sum_of_cubes_digit_list = (int(char) for char in sum_of_cubes_string)
            if collections.Counter(sum_of_cubes_digit_list) == collections.Counter(a_combination):
                print(sum_of_cubes_string)

print(calc_sum_of_powers([1, 5, 3], 3))  # should equal 153 as 153 is an armstrong number.
# number_string = '1517841543307505039'
# no_of_digits = len(number_string)
# my_counter = collections.Counter(number_string)
# print(my_counter)
# my_sum = sum([my_counter[my_digit_string] * int(my_digit_string)**no_of_digits
#            for my_digit_string in my_counter.keys()])
# print(number_string)
# print(my_sum)

# 3
# 370
# 407
# 153
# 371
# 4
# 8208
# 1634
# 9474
# 5
# 93084
# 92727
# 54748
# 6
# 548834
# 7
# 9800817
# 4210818
# 1741725
# 9926315
# 8
# 24678050
# 24678051
# 88593477
# 9
# 146511208
# 912985153
# 472335975
# 534494836
# 10
# 4679307774
# 11
# 32164049650
# 40028394225
# 42678290603
# 49388550606
# 32164049651
# 94204591914
# 44708635679
# 82693916578
# 12
# 13
# 14
# 28116440335967
# 15
# 16
# 4338281769391370
# 4338281769391371
# 17
# 35875699062250035
# 21897142587612075
# 35641594208964132
# 18
# 19
# 1517841543307505039

