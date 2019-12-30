class Solution:
    def maxProduct(self, nums) -> int:
        M =nums[0]
        cur_pro = 0
        start = 0
        end = 0
        minus = 0
        i = 0
        while i < len(nums):
            #처음 or 새로시작
            if nums[i]:
                if i == 0 or nums[i-1] == 0:
                    cur_pro = nums[i]
                    start = i
                else:
                    cur_pro*= nums[i]
                if nums[i] <0:
                    minus +=1

            if nums[i] == 0 or i == len(nums) - 1:
                end = i-1
                if nums[i] :
                    end +=1
                else:
                    M = max(0, M)
                if minus%2 == 1:
                    t = cur_pro
                    for j in range(start, end ):
                        cur_pro /= nums[j]
                        if nums[j] < 0:
                            M = max(cur_pro, M)
                            break
                    cur_pro = t
                    for j in range(end, start, -1):
                        cur_pro /= nums[j]
                        if nums[j] < 0:
                            M = max(cur_pro, M)
                            break
                M = max(cur_pro, M)
                minus = 0
                cur_pro = 0

            i+=1
        return int(M)
sol = Solution()
nums = [3,-1,4]
print(sol.maxProduct(nums))