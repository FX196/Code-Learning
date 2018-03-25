s = "733049910872815764"


def revrot(str, sz):
    if sz == 0 or len(str) == 0 or len(str) < sz:
        return ""
    n = len(str) // sz
    for i in range(n):
        s = str[i * sz:i * sz + sz]
        if sum([int(x) ** 3 for x in s]) % 2 == 0:
            s = s[::-1]
        else:
            s = s[1:] + s[0]
        str = str.replace(str[i * sz:i * sz + sz], s, 1)
    return str[:(len(str) // sz) * sz]


assert revrot(s, 5) == "330479108928157"
