class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        if not n:
            return -1
        #find mid
        left = 0
        right = n-1
        while right>left:
            mid = int((left + right) / 2)
            if nums[mid] >= nums[0]:
                left = mid
            else:
                right = mid
            if left +1 == right:
                if nums[left] < nums [right]:
                    left, right = right, 0
                break

        left, right = right, left
        print(nums[left], nums[right])

        while True:
            if right < left:
                mid = int((left + right + n) / 2)
            else:
                mid = int((left + right) / 2)
            if left == right:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                break
            if (left +1)%n == right:
                if nums[left] == target:
                    return left
                else:
                    break
            mid = mid%n
            if nums[mid] == target:
                return mid
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        return -1

sol = Solution()
nums = [1,3]
target = 3
print(sol.search(nums, target))