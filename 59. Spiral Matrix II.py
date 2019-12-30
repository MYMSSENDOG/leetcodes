class Solution:
    def generateMatrix(self, n: int):

        if n == 0:
            return
        ret = [[0]*n  for i in range(n)]
        cur_l = n
        step = 0
        number = 1
        while step < ((n + 1) //2):
            ret[step][step:step + cur_l - 1] = range(number, number + cur_l-1)
            number += cur_l - 1

            for i in range(step, step + cur_l - 1):
                ret[i][~step] = number
                number += 1

            ret[~step][step+1:step+cur_l] = reversed(range(number, number+ cur_l - 1))
            number += cur_l - 1

            for i in reversed(range(step + 1, step + cur_l)):
                ret[i][step] = number
                number += 1

            step +=1
            cur_l -= 2
        if n%2 == 1:
            ret[n//2][n//2] = n*n
        return ret
sol = Solution()
n = 3
a = sol.generateMatrix(n)
for i in a:
    print(i)

