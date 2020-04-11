class Solution:
    def summaryRanges(self, nums):
        ret = []
        if not nums:
            return []
        nums.append(nums[0])
        start = nums[0]
        prev = start
        end = start
        for i in range(1,len(nums)):
            if nums[i] == prev + 1:
                prev += 1
            else:
                end = prev
                if start == end:
                    ret.append(str(start))
                else:
                    ret.append(str(start) + "->" + str(end))
                start = nums[i]
                prev = start

        return ret



nums = [0,1,2,4,5,7]
sol = Solution()
print(sol.summaryRanges(nums))