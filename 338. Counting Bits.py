class Solution:
    def countBits(self, num: int) :
        if not num:
            return [0]
        ret = [0] * (num + 1)
        former = 0
        cur = 0
        goal = 1
        i = 1
        while i<=num:
            if i == goal:
                cur = goal
                ret[i] = 1
                goal *= 2
            else:
                ret[i] = ret[i - cur] + 1
            i+=1
        return ret



sol = Solution()
num = 10
print(sol.countBits(num))