class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        l = len(flowerbed)
        for i in range(l):
            if flowerbed[i] == 0:
                next = 0 if i == l - 1 else flowerbed[i + 1]
                last = 0 if i == 0 else flowerbed[i - 1]
                if next == 0 and last == 0:
                    flowerbed[i] = 1
                    count += 1
        return count >= n


if __name__ == "__main__":
    inp = list(map(int, input().split()))
    n = int(input())
    print(Solution().canPlaceFlowers(inp, n))
