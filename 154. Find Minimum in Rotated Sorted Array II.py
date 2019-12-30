class Solution:
    def findMin(self, nums) -> int:
        def helper(array):
            if len(array) == 1:
                return array[0]

            if array[0] != array[-1]:
                if array[0] < array[-1]:
                    return array[0]
                elif array[0] > array[-1]:
                    m =  array[0]
                    l = 1
                    r = len(array) - 1
                    mid = (r + l) // 2
                    while l < r - 1:
                        mid = (r + l) // 2
                        if array[mid] >= m:
                            l = mid
                        else:
                            r = mid

                    if array[r] >=m:
                        p = (r + 1) % len(array)
                    elif array[l] >= m:
                        p = (l + 1) % len(array)
                    else:
                        p = l
                    return array[p]
            else:
                m = len(array)//2
                return min(helper(array[:m]), helper(array[m:]))
        return helper(nums)


sol = Solution()
nums = [2,2,2,2,0]
print(sol.findMin(nums))