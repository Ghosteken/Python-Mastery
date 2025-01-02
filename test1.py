# # # # from random import choice
# # # # coin = choice(["heads","tails"])
# # # # print(coin)

# # # import random

# # # number = random.randint(1,10)

# # import random

# # cards = ["jacj","boy","do"]

# # random.shuffle(cards)
# # for card in cards:
# #     print(card)
# import statistics

# avg = statistics.mean([100,90])
# print(avg)
# '''command line arg'''
# import sys
# try:
#     print('hello  my name is', sys.argv[1])
# except IndexError:
#     print('too few args') 
import sys

if len(sys.argv) < 2:
    sys.exit("too few args")
elif len(sys.argv) > 2:
    sys.exit("too many args")

print('hello my name is', sys.argv[1])           