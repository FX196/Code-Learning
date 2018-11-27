operators = "+-*/"


def calc(expr):
    stack = []
    for token in expr.split(" "):
        if token:
            if token in operators:
                op_2 = stack.pop()
                op_1 = stack.pop()
                stack.append(eval(str(op_1) + token + str(op_2)))
            else:
                stack.append(token)
    if len(stack) == 0:
        return 0
    else:
        ans = stack.pop()
        if type(ans) == type("A"):
            return eval(ans)
        else:
            return ans


assert (calc("") == 0)
assert (calc("1 2 3") == 3)
assert (calc("1 2 3.5") == 3.5)
assert (calc("1 3 +") == 4)
