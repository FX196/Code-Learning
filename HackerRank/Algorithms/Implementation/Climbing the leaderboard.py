def climbingLeaderboard(scores, alice):
    res = []
    scores = sorted(list(set(scores)))[::-1] + [0]
    n = len(scores)
    ind = n - 1
    for score in alice:
        while scores[ind] <= score and ind > -1:
            ind -= 1
        res.append(ind + 2)
    return list(map(str, res))


if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print("\n".join(result))
