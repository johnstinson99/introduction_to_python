# CIPHERS
# http://www.math.cornell.edu/~mec/Summer2008/lundell/lecture1.html

import string

alphabet = string.ascii_uppercase
print(alphabet)
double_alphabet = alphabet + alphabet
print(double_alphabet)

def create_code_dict(offset_number):
    code_alphabet = double_alphabet[offset_number: 26 + offset_number]  # or you could use %26
    result = {}
    for i in range(26):
        result[alphabet[i]] = code_alphabet[i]
    return result

print(create_code_dict(1))


# print(translate_letter('j'))
code_dict = create_code_dict(1)
print(code_dict)

def translate_word(a_word, a_code_dict):
    letter_list = []
    for a_letter in a_word:
        if a_letter in (a_code_dict.keys()):
            letter_list.append(a_code_dict[a_letter])
        else:
            letter_list.append(a_letter)  # punctuation
    result = ''.join(letter_list)
    return result

# print(translate_word('hello'))

def translate_sentence(a_sentence, a_code_dict):
    word_list = a_sentence.split()
    # print(word_list)
    result = [translate_word(word, a_code_dict) for word in word_list]
    return result

sentence = 'hi there my friend'
sentence = 'TEXQ HFKA LC ZXHB PELRIA TB EXSB? XIFZB'
if __name__ == '__main__':
    for i in range(26):
        code_dict = create_code_dict(i)
        # print(code_dict)
        print(translate_sentence(sentence.upper(), code_dict))

# Further exercises
# Compare words to a large word list and find the best match
# Convert words to four digit numbers as per http://www.math.cornell.edu/~mec/Summer2008/lundell/lecture1.html
# to make them harder to crack
# Translate back using letter probabilities
# - first find most likely letters from a dictionary
# - check probabilities of letters in the code.
# - if one code number has more than 10%, it may be a space or word separator.
# - then take the 10 most popular letters.  Substitute them into the 5 most popular code letters in all combinations.




