class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        m = -1
        ret = ""

        def helper(A):
            ret = []
            if len(A) == 1:
                return [A]
            for i in range(len(A)):
                ret += [[A[i]] + p for p in helper(A[:i] + A[i + 1:])]
            return ret

        B = helper(A)
        print(B)
        for a, b, c, d in B:
            if 10 * a + b < 24 and 10 * c + d < 60:
                if m < 1000 * a + 100 * b + 10 * c + d:
                    m = 1000 * a + 100 * b + 10 * c + d
                    ret = str(a) + str(b) + ":" + str(c) + str(d)

        return ret