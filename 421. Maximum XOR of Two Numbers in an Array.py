class Solution:
    def findMaximumXOR(self, nums):
        ret = 0
        d = {}

        def helper(cur):
            bit = 2 ** 30
            cur_d = d
            while bit > 0:
                cur_bit = 1 if bit & cur else 0
                if cur_bit in cur_d:
                    pass
                else:
                    cur_d[cur_bit] = {}
                cur_d = cur_d[cur_bit]
                bit //= 2
        def find(cur):
            bit = 2 ** 30
            cur_d = d
            ret = 0
            while bit > 0:
                finding_bit = 0 if bit & cur else 1
                if finding_bit not in cur_d:
                    finding_bit ^= 1
                cur_d = cur_d[finding_bit]
                ret += finding_bit * bit
                bit //= 2
            return ret ^ cur


        for i in nums:
            helper(i)
        return max(find(i) for i in nums)
sol = Solution()
nums = [3, 10, 5, 25, 2, 8]
print(sol.findMaximumXOR(nums))