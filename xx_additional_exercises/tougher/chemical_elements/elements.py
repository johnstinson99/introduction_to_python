import csv
import itertools
max_word_length = 15

# READ IN ELEMENTS from elements.txt AND CREATE A DICTIONARY IN THE FORM:
# {'c': ['C', 'Carbon', '6'], 'h': ['H', 'Hydrogen', '1'], ...}
abbreviation_dict = {}
with open('elements.txt') as csv_file:
    dictreader = csv.DictReader(csv_file, delimiter='\t')
    # csv_reader = csv.reader(csv_file, delimiter='\t')
    for element_dict in dictreader:
        abbreviation_dict[element_dict['abbreviation'].lower()] = \
            [element_dict['abbreviation'],
             element_dict['name'],
             element_dict['atomic_number']]
    print(abbreviation_dict)
# lower_abbreviation_list = list(abbreviation_dict.keys())

# need list of abbreviations
# lower_abbreviation_list = [key for key in abbreviation_dict.keys()if len(key) <= 2]
# print(lower_abbreviation_list)


# First find all the permutations of 1s and 2s that add up to the full list length
def find_permutations(string_length):
    result_list = []
    for repeats in range(1,string_length+1):
        # print(repeats)
        list_of_lists = list(itertools.product([1, 2], repeat=repeats))
        for a_list in list_of_lists:
            if sum(a_list) == string_length:
                result_list.append(a_list)
    return result_list

permutation_dict = {}
for i in range(1, max_word_length + 1):
    perms = find_permutations(i)
    # print(perms)
    permutation_dict[i] = perms
print(permutation_dict)


def find_match(abbreviation):
    # lower_abbreviation = abbreviation.lower()  # Make it work with upper or lower case letters
    if abbreviation in abbreviation_dict.keys():
        return abbreviation_dict[abbreviation]
    else:
        return None


def find_string(a_string, a_permutation):
    remaining_part = a_string
    result = []
    # Check each single character or pair of characters for a match.
    for len in a_permutation:
        current_part = remaining_part[:len]
        remaining_part = remaining_part[len:]
        match_result = find_match(current_part)
        if match_result is None:  # Exit early
            return None
        else:
            result.append(match_result)
    return result


# CREATE A LIST OF ALL MATCHES. IF NO MATCHES, RETURN EMPTY LIST
def find_list_of_all_matches(a_string):
    permutations = permutation_dict[len(a_string)]
    result_list = []
    for a_permutation in permutations:
        result = find_string(a_string, a_permutation)
        if result is not None:
            result_list.append(result)
    return result_list

# FIND ALL MATCHES FOR A SINGLE WORD
# my_strings = ['beer']
# for a_string in my_strings:
#     print(find_full_match(a_string))

# FIND ALL MATCHES FOR A WORD LIST
word_list = []

with open('words_first_names.txt', mode='r') as a_file:
    csv_reader = csv.reader(a_file, delimiter=' ', skipinitialspace=True)
    for line in csv_reader:
        print(line)
        word_list.append(line[0].lower())

word_list = []
with open('words_alpha.txt', mode='r') as a_file:
    for a_line in a_file:
        a_word = a_line.strip()
        word_list.append(a_word)


# word_list = ['beer', 'accloy', 'xenoparasite', 'yardsticks', 'wiseness', 'wine', 'windsurf',
# 'vociferousness', 'intergalactic', 'alcoholic']
word_length = [len(word) for word in word_list]
print(max(word_length))
print(len(word_list))
results_list = []
with open ('results_all_words.txt', mode='w') as results_file:
    for a_string in word_list:
        if len(a_string) < max_word_length:
            result = find_list_of_all_matches(a_string)
            if result:  # If result uses the fact that an empty list returns boolean value 'False'
                print(a_string)
                print(result)
                results_list.append(a_string)
                results_file.write(a_string + ' | ' + str(result) + '\n')
print(results_list)
print(len(results_list))
print(len(word_list))
print(len(results_list)/len(word_list))