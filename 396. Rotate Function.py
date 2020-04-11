class Solution:
    def maxRotateFunction(self, A) -> int:
        s = sum(A)
        if len(A) <2:
            return 0
        first = 0
        for i in range(len(A)):
            first +=A[i] * i
        ret = first
        for i in range(len(A) - 1):
            next = first + s - len(A) * A[-1-i]
            ret = max(next, ret)
            first = next
        return ret
sol = Solution()
A = [4, 3, 2, 6]
print(sol.maxRotateFunction(A))
