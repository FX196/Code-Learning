def solution(s):
    res = []
    while len(s) >= 2:
        res.append(s[:2])
        s = s[2:]
    if s:
        res.append(s + "_")
    return res
