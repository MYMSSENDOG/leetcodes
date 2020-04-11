class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.dp = [[0]]
            return
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.dp[i][j] = self.dp[i][j-1] + self.dp[i - 1][j] - self.dp[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2][col2] + self.dp[row1-1][col1-1] - self.dp[row1-1][col2] - self.dp[row2][col1-1]


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
N = NumMatrix(matrix)
print(N.sumRegion(1,1,2,2))