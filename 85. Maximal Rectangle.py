class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        end_mat_ver = [[0]*n for i in range(m)]
        end_mat_hor = [[0] * n for i in range(m)]

        for i in range(m):
            if matrix[i][-1] == "1":
                end_mat_hor[i][-1] = n
            else:
                end_mat_hor[i][-1] = n-1
        for i in range(n):
            if matrix[-1][i] == "1":
                end_mat_ver[-1][i] = m
            else:
                end_mat_ver[-1][i] = m-1

        for i in reversed(range(m-1)):
            for j in range(n):
                if matrix[i][j] == "1":
                    end_mat_ver[i][j] = end_mat_ver[i+1][j]
                else:
                    end_mat_ver[i][j] = i

        for i in range(m):
            for j in reversed(range(n-1)):
                if matrix[i][j] == "1":
                    end_mat_hor[i][j] = end_mat_hor[i][j+1]
                else:
                    end_mat_hor[i][j] = j


        ret = 0
        for si in range(m):
            for sj in range(n):
                if matrix[si][sj] == 0:
                    continue
                stack = [-1]
                heights = []
                for ei in range(si,end_mat_ver[si][sj]):
                    heights.append(end_mat_hor[ei][sj]-sj)
                heights.append(0)
                for i in range(len(heights)):
                    while heights[i] < heights[stack[-1]]:
                        h = heights[stack.pop()]
                        w = i - stack[-1] - 1
                        ret = max(ret, h * w)
                    stack.append(i)
                heights.pop()

        return ret



sol = Solution()
n = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(sol.maximalRectangle(n))