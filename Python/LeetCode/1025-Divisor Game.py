class Solution:
    def __init__(self):
        self.d = {2: True, 3: False}

    def divisorGame(self, N: int) -> bool:
        if N in self.d.keys():
            return self.d[N]
        else:
            for i in range(1, N):
                if N % i == 0:
                    if not self.divisorGame(N - i):
                        self.d[N] = True
                        return True
            self.d[N] = False
            return False
