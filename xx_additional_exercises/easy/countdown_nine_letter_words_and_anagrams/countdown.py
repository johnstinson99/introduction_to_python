# 1)
# files: reading
# strings: len(), stripping white space
# lists: appending, slicing
# 2)
# importing
# random.choice()
# 3)
# random.sample()
# strings: ''.join()
# 4)
# math.factorial()
# 5a)
# strings: sorted(), ''.join()
# lists: comprehensions, slices
# sets: converting list to set
# 5b)
# dictionaries: creating a dictionary using a list comprehension
# 5c)
# dictionaries: for key, value in word_dict.items():
# 5d)
# dictionaries: values()



# 1) Read in file of all words and create list of 9 letter words.
nine_letter_word_list = []
with open('words_alpha.txt', mode='r') as word_file:
    for line in word_file:
        word = line.strip()
        if len(word) == 9:
            nine_letter_word_list.append(word)

print(len(nine_letter_word_list))
print(nine_letter_word_list[:10])


# 2) Choose a random word from the list and print it out.  Import the random package and use random.choice()
import random
a_word = random.choice(nine_letter_word_list)
print(a_word)


# 3) turn the word into an anagram - method 1, using random.sample()
character_list = random.sample(a_word, len(a_word))
print(character_list)
anagram = ''.join(character_list)
print(anagram)

# turn the word into an anagram - method 2 - every permutation suing itertools.permutations
# import itertools
# permutations = itertools.permutations(a_word, 9)
# # itertools.permutations returns a 'permutation' object. We can iterate through it in the same way as a list.
# # http://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
# strings_list = [''.join(permutation) for permutation in permutations]
# # print the first ten elements
# print(strings_list[:10])
# print(len(strings_list))
# # choose an anagram at random.
# print(random.choice(strings_list))

# 4) import the math library and find the factorial method.  Use it to calculate 9 factorial (9*8*7.. *2*1)
# and check the number of permutations of nine character letters.
import math
print(math.factorial(9))


# 5) Find words that match the following anagrams:
# 'ardgageun'  'cksaiottl' 'gpmsnigli'

# Method 1 - sorting letters
# 5a - first create a list of 9 character strings, with sorted letters
# use the sorted function to create a list of sorted lists of characters, for each word in the nine_letter_word_list
list_of_nine_character_words_with_sorted_letters = [''.join(sorted(word)) for word in nine_letter_word_list]
# print the first ten elements of the list.
# convert the list of characters lists, into a list of strings, using ''.join()
# print the first ten elements of the list.
print(list_of_nine_character_words_with_sorted_letters[:10])
# convert the list to a set using set()
my_set = set(list_of_nine_character_words_with_sorted_letters)
# print the length of the set using len().
print(len(my_set))
# Compare this to the length of the list of original words. Are some nine letter words anagrams of each other?

# 5b) Create a dictionary with the key being the string of sorted letters
# start with a key for each item, and the value being an empty list [] for each one.
word_dict = {sorted_char_string: [] for sorted_char_string in my_set}
# for each word in the nine_letter_word_list, add the word to the dictionary using word_dict[key] = word
# create the key using ''.join(sorted(word))
for word in nine_letter_word_list:
    sorted_char_string = ''.join(sorted(word))
    word_dict[sorted_char_string].append(word)

print('===============')

print(word_dict[''.join(sorted('gpmsnigli'))])

# 5c print all the items in the dictionary where the length of the value list is greater than one.
for key, value in word_dict.items():
    if len(value) > 1:
        print(key, value)

# 5d)
# create a list of the lengths of strings
length_list = [len(value) for value in word_dict.values()]
# find the max length
max_len = max(length_list)
print(max_len)
# find the longest list of 9 letter words that are all anagrams of each other
long_ones = [(key, value) for key, value in word_dict.items() if len(value) == max_len]
print(long_ones)

# aegilnrwy ['lawyering', 'wearingly']
# aeegillrs ['allergies', 'galleries']
# aadilmnns ['islandman', 'mainlands']
# acehorrst ['carthorse', 'horsecart', 'orchestra']





# METHOD 2 - USING collections.Counter()
# first convert the anagram to a Counter object by importing 'collections' and using collections.Counter()
# import collections
# my_counter = collections.Counter('cksaiottl')
# print(my_counter)
#
# # create a list of tuples (<counter>, <nine_letter_word>) from the nine_letter_word_list
# counter_word_tuple_list = [(collections.Counter(nine_letter_word), nine_letter_word)
#                            for nine_letter_word in nine_letter_word_list]
# # create a list of tuples where the counter (the zeroth element of the tuple), matches
# # the counter for the anagram.
# matches = [tuple for tuple in counter_word_tuple_list if tuple[0] == my_counter]
# print(matches)
#
# # Find the number of unique letter combinations
# # find all the counters:
# counter_list = [collections.Counter(nine_letter_word)
#                 for nine_letter_word in nine_letter_word_list]
# elements_list = [counter.elements for counter in counter_list]
# print(elements_list[:10])

