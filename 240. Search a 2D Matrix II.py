class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        col_boundary = 0
        row_boundary = 0
        for i, num in enumerate(matrix[0]):
            if num == target:
                return True
            if num<target:
                col_boundary+=1
            else:
                break
        for i, num in enumerate(matrix[col][0] for col in range(m)):
            if num == target:
                return True
            if num<target:
                row_boundary +=1
            else:
                break
        if not col_boundary:
            return False
        for i in range(row_boundary):
            for j in range(col_boundary):
                if matrix[i][j] == target:
                    return True
        return False
sol = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
matrix = [[5,5]]
target = 7
print(sol.searchMatrix(matrix,target))