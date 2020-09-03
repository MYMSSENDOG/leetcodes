class Solution:
    def findDiagonalOrder(self, nums):
        l = 0
        for row in nums:
            l += len(row)
        ret = [0] * l
        to_del = []
        idx = 0
        mat_i = [0] * l
        start = 0
        while start < len(nums) - 1:
            for n in range(start, -1, -1):
                if mat_i[n] >=len(nums[n]):
                    to_del.append(n)
                    continue
                else:
                    ret[idx] = nums[n][mat_i[n]]
                    mat_i[n] +=1
                    idx +=1
            start = start + 1 - len(to_del)
            for _ in range(len(to_del)):
                t = to_del.pop(0)
                nums.pop(t)
                mat_i.pop(t)
        while idx<len(ret):
            for n in range(len(nums)-1,-1,-1):
                if mat_i[n] ==len(nums[n]):
                    to_del.append(n)
                    continue
                else:
                    ret[idx] = nums[n][mat_i[n]]
                    mat_i[n] +=1
                    idx +=1
            for _ in range(len(to_del)):
                t = to_del.pop(0)
                nums.pop(t)
                mat_i.pop(t)
        return ret





sol = Solution()
nums = [[1,2,3,4,5],
        [6,7],
        [8],
        [9,10,11],
        [12,13,14,15,16]]
print(sol.findDiagonalOrder(nums))
#[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]


