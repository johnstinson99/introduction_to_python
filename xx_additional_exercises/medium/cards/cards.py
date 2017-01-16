# (value, name, suit)
import itertools
import random

pack_of_cards_list = []
for suit in ('clubs', 'diamonds', 'hearts', 'spades'):
    for value in range(1,14):
        pack_of_cards_list.append((value, suit))
pack_of_cards_set = set(pack_of_cards_list)

hand_set_1 = set(random.sample(pack_of_cards_set, 7))
remaining_cards = pack_of_cards_set.difference(hand_set_1)
print(hand_set_1)

print(len(remaining_cards))
hand_set_2 = set(random.sample(remaining_cards, 7))
print(hand_set_2)

# Combinations
# 7 out of 52
hands = list(itertools.combinations(pack_of_cards_list, 7))  # [:13]
# print(hands)
print(hands[:3])
print(len(hands))
