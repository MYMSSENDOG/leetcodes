import collections
class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        if not A and not B and not C and not D:
            return 0
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for a in A:
            for b in B:
                d1[a+b] +=1
        for c in C:
            for d in D:
                d2[c+d] +=1
        ret = 0
        for k, val in d1.items():
            if -k in d2:
                ret += d2[-k] * val
        return ret


sol = Solution()
A = [ 0,0,1]
B = [0,0,-1]
C = [0,0]
D = [ 0,0]
print(sol.fourSumCount(A,B,C,D))