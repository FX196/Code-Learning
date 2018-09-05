def sherlockAndAnagrams(s):
    substrings = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = "".join(sorted(list(s[i:j])))
            if sub not in substrings.keys():
                substrings[sub] = 0
            else:
                substrings[sub] += 1
    res = int(sum([(x + 1) * x / 2 for _, x in substrings.items()]))
    return res


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
