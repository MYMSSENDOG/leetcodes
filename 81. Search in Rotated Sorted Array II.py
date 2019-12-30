class Solution:
    def search(self, nums, target: int) -> bool:
        #n[i] > n[i+1] 이 되는 지점을 찾는다.
        #n[0] 과 n[i]를 비교 해서 0보다 작으면 재배치 후 0의 자리 밑에서 검색
        #i보다 크면 리턴 False

        for i in range(len(nums)-1):
            if nums[i] == target or nums[i+1] == target:
                return True
            if nums[i] > nums[i+1]:
                nums = nums[i+1:] + nums[0:1+i]
                break

        left = 0
        right = len(nums) - i if i != 0 else len(nums) - 1
        if target > nums[right] or target < nums[left]:
            return False
        while right > 1 + left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid
            elif nums[mid]<target:
                left = mid
        if target != nums[left] and target != nums[right]:
            return False
        return True
sol = Solution()
nums = [1,1,1,2]
target = 2
print(sol.search(nums,target))