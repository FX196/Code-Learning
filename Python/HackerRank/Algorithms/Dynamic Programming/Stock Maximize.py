#!/bin/python3

def stockmax(prices):
    max_so_far = 0
    profit = 0
    for price in prices[::-1]:
        max_so_far = max(max_so_far, price)
        profit += max_so_far - price
    return profit


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        prices = list(map(int, input().strip().split(' ')))
        result = stockmax(prices)
        print(result)