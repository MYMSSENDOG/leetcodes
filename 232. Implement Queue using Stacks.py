class MyQueue:

    def __init__(self):
        self.q1 ,self.q2 = [], []

    def push(self, x: int) -> None:
        while self.q2:
            self.q1.append(self.q2.pop())
        self.q1.append(x)

    def pop(self) -> int:
        while self.q1:
            self.q2.append(self.q1.pop())
        return self.q2.pop()

    def peek(self) -> int:
        while self.q1:
            self.q2.append(self.q1.pop())
        return self.q2[-1]

    def empty(self) -> bool:
        return not (self.q1 or self.q2)


