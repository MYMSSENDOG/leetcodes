class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        s_a = (C - A) * (D - B)
        s_b = (G - E) * (H - F)

        x = [A,C,E,G]
        y = [B,D,F,H]
        x.sort()
        y.sort()
        if (x[0], x[1]) == (A,C) or (x[0], x[1]) == (E, G):
            return s_a + s_b
        if (y[0], y[1]) == (B,D) or (y[0], y[1]) == (F, H):
            return s_a + s_b
        else:
            return s_a + s_b - (x[2] - x[1]) * (y[2] - y[1])

sol = Solution()
A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2
print(sol.computeArea(A,B,C,D,E,F,G,H))