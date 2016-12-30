print('hello there')
import numpy as np

my_dict = {0:'Thomas', 1:'Matthew', 2:'Ben'}
for element_number in range(3):
    random_string = np.random.choice(["I like","I don't like"])
    print(element_number, random_string, my_dict[element_number])