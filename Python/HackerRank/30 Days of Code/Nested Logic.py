a = [int(n) for n in input().split(" ")]
e = [int(n) for n in input().split(" ")]
s = ''

if a[2] > e[2]:
    s = '10000'
elif a[2] == e[2]:
    if a[1] > e[1]:
        s = str((a[1] - e[1]) * 500)
    elif a[1] == e[1]:
        if a[0] > e[0]:
            s = str((a[0] - e[0]) * 15)
if s:
    print(s)
else:
    print('0')
