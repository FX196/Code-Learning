from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold = 0
        bought = -prices[0]

        for price in prices[1:]:
            sold, bought = (
                max(sold, bought + price - fee),
                max(bought, sold - price))
        return sold


l = [1, 3, 2, 8, 4, 9]
fee = 2

s = Solution()
print(s.maxProfit(l, fee))
