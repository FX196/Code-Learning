def solution(args):
    args.sort()
    res = ""
    cont = False
    for i in range(len(args) - 1):
        if int(args[i]) == (int(args[i + 1] - 1)):
            if cont:
                pass
            else:
                res += str(args[i]) + "-"
                cont = True
        else:
            if cont:
                cont = False
            res += str(args[i]) + ","
    if res[-1] == "-":
        res += str(args[-1])
    else:
        res += str(args[i])
    if "," in res:
        for s in res.split(","):
            if "-" in s:
                sp = s.split("-")
                n = None
                for num in sp:
                    if num and not n:
                        n = num
                    elif num and num == n + 1:
                        res.replace(s, s)


assert (solution(
    [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) == '-6,-3-1,3-5,7-11,14,15,17-20')
assert (solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) == '-3--1,2,10,15,16,18-20')
