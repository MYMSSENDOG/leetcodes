# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        a = rand7() - 1
        b = rand7() - 1
        r = a * 7 + b
        while r >=40:
            a = b
            b = rand7() - 1
            r = a * 7 + b
        return r % 10 + 1