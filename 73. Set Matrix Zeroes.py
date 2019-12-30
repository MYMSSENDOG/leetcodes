class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        zero_row = []
        zero_col = []
        for rowi ,row in enumerate(matrix):
            for coli, element in enumerate(row):
                if element == 0:
                    if rowi not in zero_row:
                        zero_row.append(rowi)
                    if coli not in zero_col:
                        zero_col.append(coli)
                continue

        temp = len(zero_row)


        for i in zero_row:
            matrix[i] = [0]*len(matrix[0])
        for i in range(len(matrix)):
            if i not in zero_row:
                zero_row.append(i)
        zero_row = zero_row[temp:]
        for i in zero_col:
            for j in zero_row:
                matrix[j][i] = 0
                """
        isZero = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if i == 0:
                isZero = True
                break
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,j):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if isZero:
            for i in range(m):
                matrix[i][0] = 0

        print(matrix)
sol = Solution()
n = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
sol.setZeroes(n)