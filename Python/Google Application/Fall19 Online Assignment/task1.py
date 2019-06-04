# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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


print(solution("abcdefghijklmnopqrstuvwxyz", "dba"))