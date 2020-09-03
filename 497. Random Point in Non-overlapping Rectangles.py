import random
class Solution:
    def __init__(self, rects):
        self.valid_rects = []
        self.count = 0
        for rect in rects:
            x1,y1 = rect[0], rect[1]
            x2,y2 = [rect[2], rect[3]]
            self.valid_rects.append([self.count + (y2-y1+1) * (x2-x1+1), [x1,y1,x2,y2]])
            self.count = self.valid_rects[-1][0]

    def pick(self):
        rand = random.randint(1, self.count)
        vr = self.valid_rects
        l = 0
        r = len(vr)
        m = (l + r) // 2
        while r > l :
            m = (l + r) // 2
            if vr[m][0] < rand:
                l = m+1
            else:
                r = m
        d = vr[l][0] - rand
        x1,y1,x2,y2 = vr[l][1]
        y = y1 +  d//(x2 - x1+1)
        x = x1 + d % (x2-x1+1)
        return [x,y]




codes = ["Solution","pick","pick","pick"]
args =[[[[-2, -2, -1, -1], [1, 0, 3, 0]]], [], [], [], [], []]
sol = Solution(args[0][0])
for i, e in enumerate(codes, 1):
    if e == "pick":
        print(sol.pick())
