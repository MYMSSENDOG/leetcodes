class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0
        ab = a | b
        biggest = a|b|c
        bit = 1
        while bit < biggest:
            if ab&bit == c&bit:
                pass
            else:
                if c&bit:
                    ret +=1
                else:
                    if a&bit:
                        ret +=1
                    if b & bit:
                        ret += 1
            bit *= 2
        return ret
sol = Solution()
a = 1
b = 2
c = 4
print(sol.minFlips(a,b,c))