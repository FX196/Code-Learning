# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import functools

import numpy as np


def solution(keys, msg):
    # write your code in Python 3.6
    if not msg:
        return 0
    indices = {key: ind for ind, key in enumerate(keys)}
    res = prev = indices[msg[0]]
    for char in msg[1:]:
        res += abs(prev - indices[char])
        prev = indices[char]
    return res


def solution_one(keys, msg):
    return np.sum(np.abs(np.diff([0] + list(map(functools.lru_cache(None)(lambda char: keys.find(char)), list(msg))))))


print(solution("abcdefghijklmnopqrstuvwxyz", "dba"))
print(solution_one("abcdefghijklmnopqrstuvwxyz", "dba"))

import time
start = time.time()
for _ in range(100000):
    solution("abcdefghijklmnopqrstuvwxyz", "dba")
end = time.time()
print(end-start)