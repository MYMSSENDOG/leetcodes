class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(m, start):
            if m == 1:
                return 1
            elif m == 2:
                if start == "left":
                    return 2
                else:
                    return 1

            if start == "left":
                return 2 * helper(m//2, "right")
            else:
                if m % 2 == 1:
                    return 2 * helper(m//2,"left")
                else:
                    return 2 * helper(m // 2, "left") - 1
        return helper(n,"left")
n = 7
sol = Solution()
print(sol.lastRemaining(n))