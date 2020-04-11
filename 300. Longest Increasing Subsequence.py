class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        max_length = [1]
        if not nums:
            return 0
        def dfs(length, idx):#현재길이 , 다음번 idx
            max_length[0] = max(max_length[0], length + 1)
            if idx == len(nums):
                return
            cur = nums[idx]
            m = 9999999
            i = idx
            while i + max_length[0]-(length + 1) < len(nums):
                if nums[i] > cur and m > nums[i]:
                    m = nums[i]
                    dfs(length+1, i)
                i+=1
        i = 0
        while i + max_length[0]<n:
            while i + 1 < n and nums[i] > nums[i + 1]:
                i+=1
            m = 9999999
            cur = nums[i]
            while i + max_length[0] - 1 < n:
                if nums[i] > cur and m > nums[i]:
                    m = nums[i]
                    dfs(1, i)
                i+=1
        return max_length[0]


sol = Solution()
nums = [1,651,321,51,65,1,49,498,1,651,51,651,0,320,323,230,320,1,1,1,1651,61,65,1,0,32,32,5,0,9849416,651515,6516513,198116,32123,1651651,1981,132,31,519,819,1,5,6,8,4,5,6,165,165,6,3,321,21,5,8,15]

print(sol.lengthOfLIS(nums))