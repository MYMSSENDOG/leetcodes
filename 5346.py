class Solution:
    def closestDivisors(self, num: int):
        n1 = (num+1)
        n2 = (num+2)
        ret =[1, num+2]
        for i in reversed(range(1, int((num+1)**(1/2)) + 1)):
            if n1 % i == 0:
                ret = (i, n1//i)
                break
        for i in reversed(range(1, int((num+2)**(1/2)) + 1)):
            if n2 % i == 0:
                if ret[1] - ret[0] > n2//i - i:
                    ret = (i, n2//i)
                    break
        return ret


sol = Solution()
num = 9
print(sol.closestDivisors(num))

"""


a b c d e ...
2*sum - i

"""