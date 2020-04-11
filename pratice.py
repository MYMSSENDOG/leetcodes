class Solution:
    def dfs_combination(self, n, k):
        pass
    def bfs_combination(self, n, k):
        pass

    def dfs_permutation(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]



    def bfs_permutation(self, n):
        q = [[i] for i in range(1,n+1)]
        ret = []
        while q:
            for i in range(len(q)):
                t = q.pop(0)
                for j in range(1,n+1):
                    if j not in t:
                        if len(t) == n-1:
                            ret.append(t + [j])
                        else:
                            q.append(t + [j])
        return ret






sol = Solution()
n = 3
k = 2
nums = [1,2,3]
print(sol.dfs_permutation(n))