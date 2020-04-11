import bisect
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        if not nums1 or not nums2:
            return []

        d = {(0, 0): 1}
        r = 0
        q = [[r, 0, 0]]

        i, j = 0,0
        m, n = len(nums1), len(nums2)
        ret = []
        for _ in range(k):
            if not q:
                break
            t, x, y = q.pop(0)
            if x < m - 1 and (x + 1, y) not in d:
                item = [nums1[x + 1] + nums2[y], x + 1, y]
                bisect.insort(q, item)
                d[(x + 1, y)] = 1
            if y < n - 1 and (x, y + 1) not in d:
                item = [nums1[x] + nums2[y + 1], x, y + 1]
                bisect.insort(q, item)
                d[(x, y + 1)] = 1

            ret.append([nums1[x], nums2[y]])
        return ret

sol = Solution()
nums1 = [1,2,3]
nums2 = [3,5,7,9]
k = 5
print(sol.kSmallestPairs(nums1, nums2, k))