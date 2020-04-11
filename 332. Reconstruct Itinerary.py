import collections
class Solution:
    def findItinerary(self, tickets):
        def dfs(dict, route):
            start = route[-1]
            if len(route) == len(tickets) + 1:
                return route
            for i in range(len(dict[start])):
                end = dict[start][i]
                t = dict[start]
                dict[start] = dict[start][:i] + dict[start][i+1:]
                result = dfs(dict, route + [end])
                if result:
                    return result
                dict[start] = t


        d = collections.defaultdict(list)
        for s,e in tickets:
            d[s] += [e]
        for start in d:
            d[start].sort()
        s = "JFK"
        return dfs(d, [s])

sol = Solution()
tickets= [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(sol.findItinerary(tickets))