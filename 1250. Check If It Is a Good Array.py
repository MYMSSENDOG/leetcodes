class Solution:
    def isGoodArray(self, nums) -> bool:
        def gcd(n1, n2):
            n = max(n1,n2)
            d = min(n1,n2)
            if d == 0:
                return 1
            while n % d != 0:
                r = n % d
                n = d
                d = r
            return d
        g = nums[0]
        for i in range(1,len(nums)):
            g = gcd(g, nums[i])
            if g == 1:
                return True
        if g== 1:
            return True
        return False

sol = Solution()
nums = [6,10,15]
print(sol.isGoodArray(nums))