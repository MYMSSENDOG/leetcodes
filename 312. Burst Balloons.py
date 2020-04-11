class Solution:
    def maxCoins(self, nums) -> int:

        s =""
        for i in nums:
            s += chr(i)

        s = chr(1) + s + chr(1)

        memo = {'\x01\x01': 0}
        def dfs(s):
            if s in memo:
                return memo[s]
            ret = 0
            for i,e in enumerate(s[1:-1],1):
                ret = max(ret, ord(s[i]) * ord(s[i-1]) *ord(s[i+1]) + dfs(s[:i] + s[i+1:]))
            memo[s] = ret
            return ret
        return dfs(s)


sol = Solution()
nums = [3,9,3]
print(sol.maxCoins(nums))