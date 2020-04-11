class Solution:
    def thirdMax(self, nums):

        f, s, t = None,None,None
        for i in nums:
            if f == None:
                f = i
            elif s== None:
                if f == i:
                    continue
                if i > f:
                    f, s = i, f
                else:
                    s = i
            elif t== None:
                if i == s or i == f:
                    continue
                if i < s:
                    t = i
                elif s<i<f:
                    s,t = i,s
                else:
                    f, s, t = i, f, s
            else:
                if i == f or i == t or i == s or i < t:
                    continue
                if i <s:
                    t = i
                elif i < f:
                    s, t = i, s
                else:
                    f, s ,t = i, f, s
        if t!=None:
            return t
        return f

sol = Solution()
nums =[3,3,4,3,4,3,0,3,3]
print(sol.thirdMax(nums))
