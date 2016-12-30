import string

letter_list = []
with open('words_alpha.txt', mode='r') as word_file:
    for line in word_file:
        stripped = line.strip()
        letter_list += stripped

print(letter_list[:100])

total_letters = len(letter_list)

prob_list = []
for letter in string.ascii_lowercase:
    # print(letter, letter_list.count(letter)/total_letters)
    prob_list.append((letter, letter_list.count(letter)/total_letters))

print(prob_list)

def second_item(a_tuple):
    return a_tuple[1]


prob_list.sort(key=second_item, reverse=True)
print(prob_list)
# BUT dictionary isn't realistic example of real text..


