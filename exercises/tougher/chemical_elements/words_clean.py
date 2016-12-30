# i = 0
with open('words_alpha.txt', 'w') as write_file:
    with open('words_with_punctuation.txt', 'r') as my_file:
        for line in my_file:
            # i += 1
            # if i > 1000:
            #     break
            stripped_line = line.strip()
            if stripped_line.isalpha():
                # print(stripped_line)
                write_file.write(stripped_line+'\n')
