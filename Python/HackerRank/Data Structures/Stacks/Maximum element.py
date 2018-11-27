class StackNode:
    def __init__(self, data, next, curMax):
        self.data = data
        self.next = next
        self.curMax = curMax


class Stack:
    def __init__(self):
        self.top = None
        self.curMax = 0

    def push(self, data):
        self.top = StackNode(data, self.top, self.curMax)
        self.curMax = max(self.top.data, self.curMax)

    def pop(self):
        self.curMax = self.top.curMax
        self.top = self.top.next


n = int(input())
stack = Stack()

for _ in range(n):
    q = input()
    if q[0] == "1":
        stack.push(int(q.split(" ")[1]))
    elif q[0] == "2":
        stack.pop()
    else:
        print(stack.curMax)
