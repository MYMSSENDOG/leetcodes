class Solution:
    def minimumDistance(self, word: str):
        def cost(prev, next):
            if prev == 26:
                return 0
            return abs(prev//6 - next // 6) + abs(prev%6 - next%6)
        dp = [[[0]*301for i in range(27)]for j in range(27)]

        def helper(left, right, pos):
            if pos >= len(word):
                return 0
            if dp[left][right][pos] == 0:
                next = ord(word[pos]) - ord("A")
                dp[left][right][pos] = min(cost(left, next) + helper(next, right, pos+1), cost(right,next)+ helper(left,next,pos+1))+1
            return dp[left][right][pos]
        return helper(26,26,1) -1
        """
        def get_pos(alpha):
            n = ord(alpha) - ord("A")
            x = n //6
            y = n % 6
            return [x,y]
        def differ(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        dic = {}
        for i in range(26):
            idx = chr(i + ord("A"))
            dic[idx] = {}
            for j in range(26):
                _idx = chr(j + ord("A"))
                dic[idx][_idx] = differ(get_pos(idx), get_pos(_idx))
        """





sol = Solution()
word = "CAKE"
print(sol.minimumDistance(word))