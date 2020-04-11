class Solution:
    def integerReplacement(self, n: int) -> int:
        ret = 0
        while n != 1:
            if n % 2 == 0:
                ret +=1
                n = n//2
                continue
            if n == 3:
                return ret + 2

            if n & 3 == 3:
                n +=1
            else:
                n -=1
            ret +=1
        return ret







sol = Solution()
n = 100000000
print(sol.integerReplacement(n))