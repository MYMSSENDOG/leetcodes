class Solution:
    def canJump(self, nums) -> bool:
        """
        n = len(nums)
        if n == 1:
            return True
        ret = [False ]*n
        for i in reversed(range(n - 1)):
            if nums[i] + i >= n-1:
                ret[i] = True
            if ret[i] == True:
                for j in range(0,i):
                    if j + nums[j] >= i:
                        ret[j] = True
        return ret[0]
        """
        n = len(nums)
        if n == 1:
            return True
        cur = 0
        r = nums[0]
        while True:
            if r >= n-1:
                return True
            elif cur == r:
                return False
            temp = max(i + nums[i] for i in range(cur,r + 1))
            # maxd = max(i + nums[i] for i in range(l, reachable + 1))
            cur = r
            r = temp
            """
            
            
            
            """
nums = [2,3,1,1,4]
sol = Solution()
print(sol.canJump(nums))
