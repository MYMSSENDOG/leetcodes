=

class Solution:
    def countSmaller(self, nums):
        def sort(indexes):
            half = len(indexes)//2
            if half:
                left = sort(indexes[:half])
                right = sort(indexes[half:])
                for i in range(len(indexes))[::-1]:
                    if not right or (left and nums[left[-1]] > nums[right[-1]]):
                        ret[left[-1]] += len(right)
                        indexes[i] = left.pop()
                    else:
                        indexes[i] = right.pop()
            return indexes

        ret = [0] * len(nums)
        sort([i for i in range(len(nums))])
        return ret

sol = Solution()
nums = [5,2,6,1]
print(sol.countSmaller(nums))