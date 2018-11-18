class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [0]
        visited = set()
        new = True
        while new:
            new = False
            for key in keys:
                if key not in visited:
                    new = True
                    keys += rooms[key]
                    visited.add(key)
            keys = sorted(list(set(keys)))
        return len(visited) == len(rooms)
