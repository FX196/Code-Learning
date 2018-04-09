#!/bin/python3

def abbreviation(a, b):
    for c in a:
        if b and c.upper() == b[0]:
            b = b[1:]
        elif c == c.upper():
            if not b or c != b[0]:
                return "NO"
    if not b:
        return "YES"
    return "NO"


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a = input().strip()
        b = input().strip()
        result = abbreviation(a, b)
        print(result)

# some don't work
