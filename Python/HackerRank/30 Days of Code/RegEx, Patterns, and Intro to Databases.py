#!/bin/python3

names = []
N = int(input().strip())
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    if emailID.find("@gmail.com") != -1:
        names.append(firstName)
names.sort()
for name in names:
    print(name)
