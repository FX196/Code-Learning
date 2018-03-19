def to_weird_case(string):
    res = ""
    up = True
    for s in string:
        if s == " ":
            up = True
            res += " "
        elif up:
            res += s.upper()
            up = not up
        else:
            res += s.lower()
            up = not up
    return res