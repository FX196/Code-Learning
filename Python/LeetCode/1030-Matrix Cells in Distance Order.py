import heapq


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        q = heapq.heapify([])
        for i in range(R):
            for j in range(C):
                heapq.heappush(q, (abs(i - r0) + abs(j - c0), [i, j]))

        res = []
        while q:
            res.append(heapq.heappop(q))
        return res
