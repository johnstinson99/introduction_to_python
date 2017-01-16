import csv

encoded_string = '4251 4135 4989 5045 4846 3534 4535 4989 4938 4545 5089 5045 5331 4834 8950 ' \
                 '3835 8946 4548 5089 3144 3489 4935 3543 4989 5045 8949 3943 4642 5589 3439 ' \
                 '4931 4646 3531 4889 3944 5045 8950 3835 8949 5148 3631 3335 8931 4434 8944 ' \
                 '4550 8935 5446 4245 3435 7089 3251 5089 5038 3589 4938 4550 4989 3445 8936 ' \
                 '3944 3489 5038 3539 4889 4331 4841 8931 4434 8938 3152 3589 3745 4435 8939 ' \
                 '4450 4589 5038 3589 3554 3831 5149 5089 4645 4850 8931 4434 8931 4835 8938 ' \
                 '3531 3439 4437 8936 4548 8950 3835 8943 3139 4489 4835 3133 5045 4870'

# convert the code to a list of two digit pairs in the form ['42', '51', '41' ... ]
encoded_list_of_4_character_strings = encoded_string.split(' ')
print(encoded_list_of_4_character_strings)
list_of_2_character_strings = []
for four_character_string in encoded_list_of_4_character_strings:
    list_of_2_character_strings.append(four_character_string[:2])
    list_of_2_character_strings.append(four_character_string[2:])

print('list_of_2_character_strings')
print(list_of_2_character_strings)
total_number_of_2_digit_codes = len(list_of_2_character_strings)

# find the unique 2-digit codes and create a frequency list
set_of_unique_two_digit_codes = set(list_of_2_character_strings)
no_of_unique_2_digit_codes = len(set_of_unique_two_digit_codes)  # 25

frequency_tuple_list = []
for two_digit_code in set_of_unique_two_digit_codes:
    frequency = list_of_2_character_strings.count(two_digit_code) / total_number_of_2_digit_codes
    frequency_tuple_list.append((frequency, two_digit_code))  # append a tuple

# sort the list with the most commonly occurring codes at the start
frequency_tuple_list.sort(reverse=True)
print(frequency_tuple_list)

# observe 89 has 18% of occurrences, the next most frequent is 10%. Replace 89 by space

# break the list at the spaces
def break_list_at_spaces(space_code, list_of_2_char_strings):
    result = []
    word_list = []
    for two_char_string in list_of_2_char_strings:
        # print(two_char_string)
        if two_char_string == space_code:
            result.append(word_list)
            word_list = []
        else:
            word_list.append(two_char_string)
    result.append(word_list)
    return result
print(list_of_2_character_strings)
list_of_word_codes = break_list_at_spaces('89', list_of_2_character_strings)
print('list_of_word_codes')
print(list_of_word_codes)

max_word_length = len(max(list_of_word_codes, key=len))
print(max_word_length)
min_word_length = len(min(list_of_word_codes, key=len))
print(min_word_length)

# find all the 2 and 3 letter words
dict_of_word_codes_by_length = {i: [] for i in range(min_word_length, max_word_length + 1)}
for a_coded_word in list_of_word_codes:
    dict_of_word_codes_by_length[len(a_coded_word)].append(a_coded_word)
print(dict_of_word_codes_by_length)

# seed the code breaking dictionary with the code for a space
code_break_dict = {'89': ' '}
def try_match(a_string, a_list_of_two_digit_codes):
    for i in range(len(a_string)):
        code_break_dict[a_list_of_two_digit_codes[i]] = a_string[i]

# start by matching 'the'
try_match('the', ['50', '38', '35'])
# # this gives us first letter of one of the two letter words 't' - likely to be 'to'
try_match('to', ['50', '45'])
# # this gives us .hoot : likely to be 'shoot'
try_match('s', ['49'])  # shoot
try_match('m', ['43'])  # seems
try_match('in', ['39', '44'])  # into
try_match('ply', ['46', '42', '55'])  # simply (or their or main nearer end)
try_match('and', ['31', '44', '34'])# and
try_match('r', ['48']) # torpedoes
try_match('w', ['53'])  # toward
try_match('c', ['33'])  # reactor
try_match('x', ['54'])  # reactor
try_match('but', ['32', '51', '50'])  # but

print(code_break_dict)

def break_code(dict, list_of_2_char_strings):
    result = []
    for two_char_string in list_of_2_char_strings:
        if two_char_string in dict.keys():
            result.append(dict[two_char_string])
        else:
            result.append('.')
    print(result)
    print(''.join(result))

break_code(code_break_dict, list_of_2_character_strings)

# with open('most_common_words', mode='r') as common_word_file:
#     dict_reader = csv.DictReader(common_word_file, delimiter='\t')
#     #for dict in dict_reader:
#         # print(dict)

