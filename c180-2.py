class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack  = []
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val



code = ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
args = [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
C = CustomStack(args[0][0])
for  i,c in enumerate(code[1:],1):
    if c == "push":
        C.push(args[i][0])
    if c =="pop":
        print(C.pop())
    if c == "increment":
        C.increment(args[i][0], args[i][1])
