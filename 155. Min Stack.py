class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:

        if len(self.stack) > 0:
            m = self.stack[-1][1]
        else:
            m = x

        self.stack.append([x, m])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

s = MinStack()
code = ["MinStack","push","push","push","getMin","pop","top","getMin"]
arg = [[],[-2],[0],[-3],[],[],[],[]]

for i,c  in enumerate(code[1:],1):
    if c == "push":
        print(s.push(arg[i]))
    elif c == "top":
        print(s.top())
    elif c == "getMin":
        print(s.getMin())
    elif c == "pop":
        print(s.pop())
