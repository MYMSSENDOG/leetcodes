class ProductOfNumbers:

    def __init__(self):
        self.q = [0]
        self.zero = 0
    def add(self, num: int) -> None:
        if num == 0:
            self.zero = 0
        else:
            self.zero +=1
        prev = self.q[-1]
        if prev == 0:
            self.q.append(num)
        else:
            self.q.append(prev * num)

    def getProduct(self, k: int) -> int:
        if self.zero < k:
            return 0
        if self.q[-k - 1] == 0:
            return self.q[-1]
        return self.q[-1] // self.q[-k - 1]

p = ProductOfNumbers()
p.add(2)
p.add(0)
p.add(2)
p.add(0)
p.add(2)
print(p.getProduct(1))
print(p.getProduct(2))
print(p.getProduct(3))
print(p.getProduct(5))
p.add(7)
p.add(6)
p.add(7)

"""
3 0 2 5 4
3 0 0 0 0

"""