def valid_parentheses(string):
    counter = 0
    for c in string:
        if c == "(":
            counter += 1
        elif c == ")":
            if not counter:
                return False
            else:
                counter -= 1
    return counter == 0
