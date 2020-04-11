class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #소인수 분해 후 각각의 것들이
        return not (n & n-1) and n != 0


sol = Solution()
n = 218
print(sol.isPowerOfTwo(n))