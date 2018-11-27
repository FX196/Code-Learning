# Problem        : Base Arithmetic
# Language       : Python 3
# Compiled Using : py_compile
# Version        : Python 3.4.3
# Input for your program will be provided from STDIN
# Print out all output from your program to STDOUT

import sys

d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10,
     "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def min_base(num):
    return 1 + max(list(map(lambda x: d[x], list(num))))


def base_sum(x, y):
    return int(x, min_base(x)) + int(y, min_base(y))


data = sys.stdin.read().splitlines()

x, y = data
print(base_sum(x, y))
