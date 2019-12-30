class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False


        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = m*n-1
        if matrix[n-1][m-1] < target or matrix[0][0] > target:
            return False

        while left + 1 <right:
            mid = (left + right) // 2
            mid_v = matrix[mid//m][mid%m]
            if target == mid_v:
                return True
            elif mid_v > target:
                right = mid
            else:
                left = mid
        if matrix[left//m][left%m] == target or matrix[right//m][right%m] == target:
            return True
        return False


matrix = [
    [1, 3, 5, 7,9],
    [10, 11, 16, 20,21],
    [23, 30, 34, 50,51]
]
target =1
sol = Solution()
print(sol.searchMatrix(matrix,target))
