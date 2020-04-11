
class Solution:
    def luckyNumbers(self, matrix) :
        if not matrix or not matrix[0]:
            return []
        ret = []
        min_in_row = []
        m = len(matrix)
        n = len(matrix[0])
        big_in_col = []
        for row in matrix:
            min_in_row.append(min(row))

        for j in range(n):
            M = -9999
            for i in range(m):
                M = max(M,matrix[i][j])
            big_in_col.append(M)
        for i in min_in_row:
            for j in big_in_col:
                if i == j:
                    ret.append(i)
        return ret
sol = Solution()
matrix = [[7,8],[1,2]]
print(sol.luckyNumbers(matrix))