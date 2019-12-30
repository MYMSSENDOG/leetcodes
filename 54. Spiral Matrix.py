class Solution:
    def spiralOrder(self, matrix):
        ret = []
        if not matrix or not matrix[0]:
            return None
        width = len(matrix[0])
        height = len(matrix)
        x = width
        y = height
        sequence = 0
        while y>0 and x > 0:
            ret +=  matrix[sequence][sequence:x + sequence]#맨윗줄

            if y == 1:
                break

            for i in matrix[sequence+1:sequence + y]:
                ret += [i[-sequence - 1]]

            if x == 1:
                break

            matrix[-sequence - 1].reverse()
            ret += matrix[-sequence - 1][sequence + 1: sequence  + x ]

            for i in matrix[height - sequence - 2 : sequence:-1]:
                ret += [i[sequence]]
            x -=2
            y -=2
            sequence +=1
        return ret

sol = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(sol.spiralOrder(matrix))