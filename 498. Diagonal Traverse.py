class Solution:
    def findDiagonalOrder(self, matrix):
        ret = []
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        dir = [[[-1,1], [0,1],[1,0]],[[1,-1],[1,0],[0,1]]]
        d = 0
        i , j = 0,0
        ret = [matrix[0][0]]
        while 1:
            for count, direction in enumerate(dir[d]):
                y, x = direction
                if 0<=i+y <m and 0<=j+x<n:
                    if count != 0:
                        d = -d + 1
                    i = i+y
                    j = j+x
                    ret.append(matrix[i][j])
                    break
            if i == m-1 and j == n-1:
                return ret

sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(sol.findDiagonalOrder(matrix))
