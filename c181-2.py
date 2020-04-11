class Solution:
    def sumFourDivisors(self, nums) -> int:
        ret = 0
        for i in nums:
            std = i ** (1/2)
            j = 2
            count = 0
            divisors = 1 + i
            while j <std:
                if i / j == int(i / j):
                    if count == 0:
                        count +=1
                        divisors += int(i / j) + j
                    else:
                        count +=1
                        break
                j+=1
            if count == 1 and std != int(std):
                ret += divisors
        return ret
sol = Solution()
nums = [7286,18704,70773,8224,91675]
print(sol.sumFourDivisors(nums))