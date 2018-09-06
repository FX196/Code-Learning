def expanded_form(num):
    res = []
    num = list(str(num))
    for i in range(len(num)):
        if int(num[-i - 1]) > 0:
            res.append(int(num[-i - 1]) * (10 ** i))
    res = list(map(str, res))
    return " + ".join(list(reversed(res)))
