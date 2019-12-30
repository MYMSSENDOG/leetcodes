class Solution:
    def twoSum(self, numbers, target: int) :
        l = 0
        r = len(numbers) - 1
        for i,e  in enumerate(numbers):
            if e > target:
                r = i
                break
        while numbers[l] +numbers[r] != target:
            sum = numbers[l] +numbers[r]
            if sum < target:
                l +=1
            elif sum == target:
                return [l+1, r+1]
            else:
                r -= 1
                l = 0
        return [l+1, r+1]



sol = Solution()
nums = [-1,0]
target = -1
print(sol.twoSum(nums, target))