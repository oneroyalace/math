import math
import random

# box = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]
# # print(len(box))
# got_2 = 0
# for _ in range(1_000_000):
#     selection = random.sample(box, k=4)
#     if sum([i == 1 for i in selection]) == 2:
#         got_2 += 1
# print(got_2)

# box = [1,2,3,4,5]

########## Hw2 #3c
# all_5 = 0
# for _ in range(10000):
#     selection = random.choices(box, k=10)
#     if all([i in selection for i in box]):
#         all_5 += 1

# print(all_5)


########## Hw2 #6
# box = [(1, "b"), (2, "b"), (3, "b"), (4, "b"), (5, "b"),
#        (1, "r"), (2, "r"), (3, "r"), (4, "r"), (5, "r")]

# joe_win, kamala_win = 0, 0

# for _ in range(100_000):
#     selection = random.sample(box, 2)
#     joe_pick, kamala_pick = selection[0], selection[1]
#     if (kamala_pick[1] == joe_pick[1]):
#         kamala_win += 1
#     else:
#         joe_win += 1


# print("kamala_win", kamala_win)
# print("joe_win", joe_win)


#### draws of k elements with duplicates given large M
### Probability of duplicate should be ~0.5 when k = sqrt(2*M*ln(2))
box = range(10_000)
M = len(box)
num_marbles_to_pick = math.floor(math.sqrt(2*M*math.log(2)))

dupe_in_draw = 0
for _ in range(1000):
    selection = random.choices(box, k=num_marbles_to_pick)
    if len(set(selection)) < len(selection):
        dupe_in_draw += 1

print(dupe_in_draw)
