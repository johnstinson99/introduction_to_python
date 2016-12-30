# from FunExercises.frequency_ciphers.frequency_tuples import get_frequency_tuples
import itertools

import exercises.tougher.letter_frequency_ciphers.frequency_tuples

# Assume first 10 all appear in the first 5
frequency_tuple_list = exercises.tougher.letter_frequency_ciphers.frequency_tuples.get_frequency_tuples()
print(frequency_tuple_list)
letters_in_frequency_order = [tuple[0] for tuple in frequency_tuple_list]
print(letters_in_frequency_order)

code = '131205260932363106051616191918230105161307094128'

# BREAK CODE DOWN INTO PAIRS OF DIGITS
code_pairs = [code[i:i+2] for i in range(0, len(code))]
print(code_pairs)
unique_codes = set(code_pairs)
print(unique_codes)
no_of_unique_codes = len(unique_codes)

# FIND FREQUENCY OF OCCURRENCE OF EACH 2 DIGIT CODE
code_list = []
for a_code in unique_codes:
    frequency = code_pairs.count(a_code)/no_of_unique_codes
    code_list.append((frequency, a_code))
code_list.sort(reverse=True)
two_digit_code_numbers_in_frequency_order = [item[1] for item in code_list]
print(two_digit_code_numbers_in_frequency_order)

letters_to_swap = 5
code_pairs_of_numbers_to_swap = 7
most_common_letters = letters_in_frequency_order[:letters_to_swap]
most_common_codes = two_digit_code_numbers_in_frequency_order[:code_pairs_of_numbers_to_swap]

# FIND ALL PERMUTATIONS OF LETTERS
# a = itertools.product(most_common_codes,most_common_letters)
list_of_letter_permutations = list(itertools.permutations(most_common_letters))
print(len(list_of_letter_permutations))
print(list(list_of_letter_permutations))

# FIND ALL COMBINATIONS OF CODES
list_of_code_combinations = list(itertools.combinations(most_common_codes, 5))
print(list_of_code_combinations)

translations = list(itertools.product(list_of_code_combinations, list_of_letter_permutations))
print(translations)

# use permutations of one (order does matter)
# and combinations of the other (order doesn't matter - just unique sets of code numbers.)

def make_translation_dict(number_list, letter_list):
    translation_dict = {}
    for i in range(letters_to_swap):
        translation_dict[number_list[i]] = letter_list[i]
    return translation_dict

def translate(code_pairs, dict):
    result = []
    for two_digit_code in code_pairs:
        if two_digit_code in dict.keys():
            result += dict[two_digit_code]
        else:
            result += '.'
    return result

for a_translation in translations:
    translation_dict = make_translation_dict(a_translation[0], a_translation[1])
    # print(translation_dict)
    translated_list = translate(code_pairs, translation_dict)
    result = ''.join(translated_list)
    print(result)

