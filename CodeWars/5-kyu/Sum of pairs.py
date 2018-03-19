l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]
def sum_pairs(ints, s):
    if len(ints)<2:
        return None
    d = set()
    for num in ints:
        needed = s-num
        if needed in d:
            return [needed, num]
        else:
            d = d.union({num})
    return None

assert(sum_pairs([1, 4, 8, 7, 3, 15],8) == [1,7])
assert(sum_pairs(l5, 10) == [3, 7])