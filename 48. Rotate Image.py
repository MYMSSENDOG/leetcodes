

class Solution:

    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n<=1:
            return

        start = 0
        end = n - 1
        while start<=end:
            i = 0
            while i < end-start:
                matrix[start][start+i], matrix[start+i][end], matrix[end][end-i], matrix[end-i][start] = \
                    matrix[end-i][start],matrix[start][start + i], matrix[start + i][end], matrix[end][end - i]
                i += 1
            start +=1
            end -=1
        print(matrix)

sol = Solution()
n = [
  [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
]
sol.rotate(n)