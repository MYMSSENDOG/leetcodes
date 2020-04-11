class Solution:
    def wiggleSort(self, nums) -> None:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        S = sum(nums)
        l = 0
        r = n - 1

        while 1:
            small , mid, big = 0,0,0
            for i in range(l, r+1):
                if nums[i] == nums[l]:
                    mid +=1
                elif mid[i] > nums[l]:
                    big+=1
                else:
                    small +=1
            if min(small, big) + mid < max(small, big):
                pass # go to final phase
            else:
                if small + mid < big:
                    pass # 작은부분 채움
                    #l += small + mid

                else:
                    pass
                    #큰부분 채움
                    #r -=  big + mid

        return nums
#inplace solution = only swap can be occured
sol = Solution()
nums = [5,6,5,6,5,6,5,4]
print(sol.wiggleSort(nums))