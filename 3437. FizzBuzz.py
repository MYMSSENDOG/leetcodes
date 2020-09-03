class Solution:
    def fizzBuzz(self, n: int):
        ret = []
        for i in range(1, n+1):
            cur = ""
            if i % 3 == 0:
                cur += "Fizz"
            if i % 5 == 0:
                cur += "Buzz"
            if not cur:
                cur = str(i)
            ret.append(cur)
        return ret