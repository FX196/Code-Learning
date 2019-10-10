from typing import List


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        root = {city: city for city in range(1, N + 1)}

        def find(city):
            if root[city] == city:
                return city
            else:
                root[city] = find(root[city])
                return root[city]

        cost = 0
        connections.sort(key=lambda x: x[2])
        for connection in connections:
            c1, c2, e_cost = connection
            if find(c1) == find(c2):
                continue
            else:
                cost += e_cost
                root[find(c1)] = find(c2)
        if len(set([find(i) for i in range(1, N + 1)])) != 1:
            return -1
        else:
            return cost
