import random
import bisect
class Solution:
    def __init__(self, rects):
        self.rects = rects[0]
        self.weight = 0
        self.q = []
        for rect in self.rects:
            x1,y1,x2,y2 = rect
            self.weight += (y2 - y1 + 1) * (x2 - x1 + 1)
            self.q.append(self.weight)

    def pick(self):
        r = random.randint(0,self.weight - 1)
        i = bisect.bisect_right(self.q, r)
        x1,y1,x2,y2 = self.rects[i]
        if i != 0:
            r -= self.q[i - 1]
        y = r // (x2 - x1 + 1) + y1
        x = r %(x2 - x1 + 1) + x1
        return [x,y]



codes = ["Solution","pick","pick","pick","pick","pick"]
args = [[[[1,1,2,2], [3,0,5,0]]],[],[],[],[],[]]
sol = Solution(args[0])
ret = []
for i in range(28):
    ret.append(sol.pick())
print(sorted(ret))


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()