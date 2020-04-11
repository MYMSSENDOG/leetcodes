class Solution:
    def circularArrayLoop(self, nums) -> bool:
        n = len(nums)
        if not n :
            return False

        for i in range(n):
            if nums[i]%n == 0:
                continue
            minus = 1 if nums[i] > 0 else -1
            j = i
            visited = [0] * n
            while visited[j] == 0:
                visited[j] +=1
                next = (j + nums[j])%n
                if nums[next] * minus < 0:
                    break
                j = next
            else:
                if nums[j]%n == 0:
                    continue
                return True
        return False
sol = Solution()
nums = [-1,-2,-3,-4,-5]
print(sol.circularArrayLoop(nums))