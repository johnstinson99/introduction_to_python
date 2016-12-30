import os
file_name = os.path.join(os.getcwd(), 'ch1_2_5_reusing_code.py')
print(file_name)

with open(file_name, 'r', encoding='utf-8') as infile:
    for line in infile:
        if 'print' in line:
            print(line)
