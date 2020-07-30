import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        d = collections.defaultdict(list)
        s = set()
        for a, b in dislikes:
            d[a].append(b)
            d[b].append(a)
            s.add(a)
            s.add(b)
        group = [{},{}]

        while s:
            to_del = set()
            q = set([s.pop()])
            idx = 0
            while q:
                idx = -idx - 1
                cur_group = group[idx]
                next = set()
                for cand in q:
                    if cand in group[idx+1]:
                        return False
                    elif cand not in cur_group:
                        cur_group[cand] = 1
                        for next_cand in d[cand]:
                            next.add(next_cand)
                s -= set(q)
                q = next
        return True
sol = Solution()
N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5]]
print(sol.possibleBipartition(N, dislikes))