# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        start = 0
        end = 10
        while 1:
            d = (end - start)/7
            r = 7
            end = start + r * d
            start =  start + (r - 1) * d
            if int(start)  == int(end) or int(start) == 9:
                return int(start) + 1
sol = Solution()
print(sol.rand10())
