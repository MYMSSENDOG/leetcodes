import collections
class Solution:
    def rankTeams(self, votes) -> str:
        d = collections.defaultdict()
        for s in votes:
            for i, c  in enumerate(s):
                if c not in d:
                    d[c] = [0] * 26
                d[c][i] -=1
        ret = []
        for c in d:
            ret.append([d[c], c])
        ret.sort()

        s = ""
        for i in range(len(ret)):
            s+= ret[i][1]
        return s


sol = Solution()
votes = ["ABC","ACB","ABC","ACB","ACB"]
print(sol.rankTeams(votes))
