# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        def isBadVersion(n):
            if n >= 1:
                return True
            return False
        l = 0
        r = n
        while l < r:
            m = (l + r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m+1
        return l



sol = Solution()
n = 7
print(sol.firstBadVersion(n))