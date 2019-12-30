def find_bigger_min(nums, i):
    l = i + 1
    r = len(nums) - 1
    while r >l:
        mid = int((r + l) / 2)
        if nums[mid] > nums[i]:
            l = mid

        else:
            r = mid
        if r - l == 1:
            if nums[i]<nums[r]:
                return r
            else:
                break
    return l

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return None
        n = len(nums)

        sorted = False
        #작아지는 시점 찾기
        # 그것보다 큰 가장 작은 값 찾기

        for i in range(n-1,0,-1):
            if nums[i] <= nums[i - 1]:
                continue
            else:
                #i 이후 다시 정렬 a + b - 1 / 2찾으면 일단 스왑
                sorted = True
                min_i = find_bigger_min(nums,i - 1)
                nums[i - 1], nums[min_i] = nums[min_i],nums[i - 1]
                for j in range(i, int((i + n +1)/ 2)):
                    nums[j], nums[i-j - 1] = nums[i-j - 1],nums[j]
                break
        if not sorted:
            nums.reverse()
        return nums
sol = Solution()
nums = [0,0,4,2,1,0]
print(sol.nextPermutation(nums))
