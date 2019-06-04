# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    k = 1  # nodes per level
    ind = 0  # current index in list
    n = len(A)  # length of list
    max_so_far = A[0]
    max_level = current_level = 1
    while ind < n:
        level_sum = sum(A[ind:ind + k])
        if max_so_far < level_sum:
            max_so_far = level_sum
            max_level = current_level
        ind += k
        k *= 2
        current_level += 1
    return max_level