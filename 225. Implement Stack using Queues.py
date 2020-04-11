class MyStack:

    def __init__(self):
        self.q = [0 for i in range(100)]
        self.front = 0
        self.rear = -1

        #pop
        #push_back
        #peek

    def push(self, x: int) -> None:
        self.q[self.front] = x
        if self.rear == -1:
            self.rear += 1
        self.front += 1


    def pop(self) -> int:
        if self.rear == -1:
            return None
        if self. rear == self.front:
            return None

        self.front -=1
        return self.q[self.front]

    def top(self) -> int:
        if self.rear == -1 or self.rear == self.front:
            return None
        return self.q[self.front-1]


    def empty(self) -> bool:
        return self.rear == -1 or self.rear == self.front

s = MyStack()
codes = ["MyStack","push","push","top","pop","empty"]
args = [[],[1],[2],[],[],[]]
for i,c in enumerate(codes[1:],1):
    if args[i]:
        arg = args[i][0]
    if c == "push":
        print(s.push(arg))
    elif c == "top":
        print(s.top())
    elif c == "pop":
        print(s.pop())
    elif c == "empty":
        print(s.empty())