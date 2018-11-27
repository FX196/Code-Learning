#!/bin/python3


def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        if grades[i] > 37 and (grades[i] % 5) > 2:
            grades[i] += (5 - grades[i] % 5)
    return grades


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
