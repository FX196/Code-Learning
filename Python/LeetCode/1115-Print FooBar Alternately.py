import time


# concurrency

class FooBar:
    def __init__(self, n):
        self.n = n
        self.status = 0

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            while self.status:
                time.sleep(0.000001)
            printFoo()
            self.status = 1

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            while not self.status:
                time.sleep(0.000001)
            printBar()
            self.status = 0
