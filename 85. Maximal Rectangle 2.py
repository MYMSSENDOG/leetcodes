class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        left = [0]*n
        right = [n]*n
        height = [0] * n
        ret = 0
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] +=1
                else:
                    height[j] = 0

            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(cur_left,left[j])
                else:
                    left[j] = 0
                    cur_left = j+1
            for j in reversed(range(n)):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                ret = max((right[j] - left[j]) * height[j],ret)
        return ret
sol = Solution()
n = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(sol.maximalRectangle(n))