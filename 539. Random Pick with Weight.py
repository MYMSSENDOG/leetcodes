import bisect
import random
class Solution:

    def __init__(self, w):
        self.q = [0]
        for i in w:
            self.q.append(i + self.q[-1])
        self.total = self.q[-1]
        self.q.pop(0)
    def pickIndex(self) -> int:
        t = random.randint(0, self.total-1)
        return bisect.bisect_left(self.q, t)
codes = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
args = [[[1,3,4]],[],[],[],[],[]]
sol = Solution(args[0][0])
for code, arg in zip(codes[1:], args[1:]):
    if code == "pickIndex":
        print(sol.pickIndex())
# Your Solution object will be
# instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()