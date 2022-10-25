
# import math
# import sys

# luku = (input("Anna luku, erottele pilkulla!: "))

# # string with commas
# # split string by comma
# ls = luku.split(" ")
# print(ls)

# pienin = min(ls)
# suurin = max(ls)
# summa = sum(ls)

# print(pienin)
# print(suurin)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("luku1", help="syota luku 1", type=int)
parser.add_argument("luku2", help="syota luku 1", type=int)
args = parser.parse_args()
print(args.luku1 + args.luku2)