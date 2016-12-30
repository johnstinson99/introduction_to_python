import os

os.system('dir')  # run system command

import sys
print(sys.modules)
print(sys.platform)
print(sys.version)


import pickle

my_list = [1, None, 'Stan']

with open('filename.pickle', 'wb') as write_file:
    pickle.dump(my_list, write_file)  # , protocol=pickle.HIGHEST_PROTOCOL

with open('filename.pickle', 'rb') as read_file:
    new_list = pickle.load(read_file)

print(new_list)

print(list(range(10)[::-1]))
print(['hello', 'there'][::-1])
my_list = list(range(10))
print(my_list)
print (my_list[-5:])