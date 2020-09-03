class Solution:
    def findDiagonalOrder(self, nums):
        ret = []
        for i, r in enumerate(nums):
            for j, n in enumerate(r):
                if len(ret) <= i + j:
                    ret.append([])
                ret[i+j].append(n)
        return [i for A in ret for i in A[::-1]]


sol = Solution()
nums = [[1,2,3,4,5],
        [6,7],
        [8],
        [9,10,11],
        [12,13,14,15,16]]
print(sol.findDiagonalOrder(nums))
#[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]


