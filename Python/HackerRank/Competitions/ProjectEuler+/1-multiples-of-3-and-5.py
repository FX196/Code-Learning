#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    total = 0
    # add multiples of 3
    n_3 = n - n % 3
    m_3 = n // 3
    total += (3 + n_3) * m_3 // 2
    # add multiples of 5
    n_5 = n - n % 5
    m_5 = n // 5
    total += (5 + n_5) * m_5 // 2
    # subtract multiples of 15
    n_15 = n - n % 15
    m_15 = n // 15
    total -= (15 + n_15) * m_15 // 2
    print(total)
