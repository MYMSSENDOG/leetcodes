class Solution:
    def maxJumps(self, arr, d: int) -> int:
        memo = {}

        def dfs(i): #i = index n = number of jump
            cur = arr[i]
            M = 0
            s_m = cur
            for j in reversed(range(max(i - d, 0),i)):
                if arr[j] > s_m:
                    s_m = arr[j]
                    if j not in memo:
                        M = max(M,dfs(j)+1)
                    else:
                        M = max(memo[j]+1, M)
            s_m = cur
            for j in range(i, min(i + d + 1, len(arr))):
                if arr[j] > s_m:
                    s_m = arr[j]
                    if j not in memo:
                        M = max(M,dfs(j)+1)
                    else:
                        M = max(memo[j]+1, M)

            memo[i] = M
            return M

        m = 0
        for i in range(len(arr)):
            dfs(i)

        for i in memo:
            m = max(memo[i], m)

        return m+1



sol = Solution()
arr = [6,4,14,6,8,13,9,7,10,6,12]


d = 2
print(sol.maxJumps(arr,d))