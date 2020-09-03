import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):

        while 1:
            x = random.uniform(- self.radius, self.radius)
            y = random.uniform(- self.radius, self.radius)
            if x *x + y * y  <= self.radius * self.radius:
                return [self.x + x, self.y + y]




codes = ["Solution","randPoint","randPoint","randPoint"]
args = [[1,0,0],[],[],[]]
sol = Solution(args[0][0],args[0][1], args[0][2])
for i, c in enumerate(codes[1:], 1):
    if c == "randPoint":
        print(sol.randPoint())
