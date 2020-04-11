import collections
class Solution:
    def calcEquation(self, equations, values, queries):


        d = collections.defaultdict(list)
        zeros = []
        for i, e in enumerate(equations):
            a, b = e
            if values[i] == 0:
                zeros.append(a)
            d[a]+= [[b, values[i]]]
            d[b] += [[a, 1/values[i]]]
        ret = []
        for a, b in queries:
            if a not in d or b not in d:
                ret.append(-1)
                continue
            if a in zeros:
                if b not in zeros:
                    ret.append(0)
                else:
                    ret.append(-1)
                continue
            else:
                added = False
                q = [[1, [a]]]
                while q:
                    for i in range(len(q)):
                        cur_v, route = q.pop(0)
                        prev = route[-1]
                        if route[-1] == b:
                            ret.append(cur_v)
                            added = True
                            break
                        for r, val in d[prev]:
                            if r in route:
                                continue
                            q.append([val * cur_v, route + [r]])
                if not added:
                    ret.append(-1)
        return ret

sol = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"], ["c","a"]]

sol = Solution()
print(sol.calcEquation(equations, values, queries))