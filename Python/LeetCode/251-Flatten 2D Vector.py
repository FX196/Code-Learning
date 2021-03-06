from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.l = sum(v, [])

    def next(self) -> int:
        return self.l.pop(0)

    def hasNext(self) -> bool:
        return not not self.l

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# just sum the lists
