import string

lower_letters_with_punctuation = string.ascii_lowercase + string.punctuation + ' '
print(lower_letters_with_punctuation)

offset = 31

encode_dict = {}
for i in range(0, len(lower_letters_with_punctuation)):
    encode_dict[lower_letters_with_punctuation[i]] = str(i+offset)
print(encode_dict[' '])

'to', 'do', # 3, 19  # be TO on in it on he as DO at
'and', 'are', 'for', 'not', 'but', 'the'  # 5, x, 12, 13, 22 ,1  # THE, AND, FOR, NOT, you, BUT, his
# that, have, with, this, from, they, what, when, make

# 1 - try one word
#   - first letter = populate all those letters in grid
#   - same for other letters one by one
# 2 - which other small words will fit into next most common one?
# try with each possible short word combination



text  = 'Lukes torpedoes shoot toward the port and seems to simply disappear into the surface and not explode. ' \
        'But the shots do find their mark and have gone into the exhaust port and are heading for the main reactor.'
lower_text = text.lower()

encoded_text_list = [encode_dict[letter] for letter in lower_text]
print(encoded_text_list)
four_letter_list = []
for i in range(int(len(text)/2)):
    four_letter_list.append(encoded_text_list[i*2] + encoded_text_list[i*2+1])
print(four_letter_list)
four_letter_string = ' '.join(four_letter_list)
print(four_letter_string)
