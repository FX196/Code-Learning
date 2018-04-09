import string


def diff(s):
    if s.count(" ") == 0:
        if s.count("x") == 0:
            return 0
        else:
            return 1
    ext = extract(s)
    if len(ext) == 3:
        op, arg1, arg2 = ext
    else:
        op, arg1 = ext
    if op == "+":
        return simp("(+ %s %s)" % (diff(arg1), diff(arg2)))
    elif op == "-":
        return simp("(- %s %s)" % (diff(arg1), diff(arg2)))
    elif op == "*":
        return simp("(+ (* %s %s) (* %s %s))" % (diff(arg1), arg2, diff(arg2), arg1))
    elif op == "/":
        return simp("(/ (- (* %s %s) (* %s %s)) (^ %s 2))" % (diff(arg1), arg2, arg1, diff(arg2), arg2))
    elif op == "^":
        if "x" in arg1.replace(")", "").split(" "):
            pass


def simp(s):
    if s.count(" ") == 0:
        return s
    else:
        ext = extract(s)
        if len(ext) == 3:
            op, arg1, arg2 = ext
            s1 = simp(arg1)
            s2 = simp(arg2)
            res = op, s1, s2
        else:
            op, arg1 = ext
            s1 = simp(arg1)
            res = op, s1
        if op == "+":
            if s1 in string.digits and s2 in string.digits:
                return str(int(s1) + int(s2))
        elif op == "-":
            if s1 in string.digits and s2 in string.digits:
                return str(int(s1) - int(s2))
        elif op == "*":
            if s1 == "0" or s2 == "0":
                return "0"
            elif s1 in string.digits and s2 in string.digits:
                return str(int(s1) * int(s2))
        elif op == "/":
            if s1 == "0":
                return "0"
        elif op == "^":
            if s2 == "1":
                return simp(arg1)
            elif s2 == "0":
                return "1"
        return "(%s)" % " ".join(res)


def extract(s):
    s = s[1:-1]
    finding = False
    count = 0
    l = s.split(" ")
    res = []
    if s.count("(") != 0:
        res.append(l[0])
        ind = len(res[0]) + 1
        temp = ""
        while ind < len(s):
            temp += s[ind]
            if s[ind] == "(":
                count += 1
                finding = True
            elif s[ind] == ")":
                count -= 1
                if count == 0:
                    res.append(temp)
                    finding = False
                    temp = ""
                    ind += 1
            ind += 1
        if temp:
            res.append(temp)
    else:
        res = l
    if len(res) == 3:
        return res[0], res[1], res[2]
    else:
        return res[0], res[1]


if __name__ == "__main__":
    s = input()
    print(diff(s))
