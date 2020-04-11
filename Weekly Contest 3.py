import collections
class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections)<n-1:
            return -1
        dic = {}
        line_dic = collections.defaultdict(list)
        for i in connections:
            line_dic[i[0]].append(i[1])
            line_dic[i[1]].append(i[0])
        ret = 0
        for i in range(n):
            q = []
            if i in dic:
                continue
            else:
                ret += 1
                dic[i] = 1
                q.append(i)
                while q:
                    for j in range(len(q)):
                        cur = q.pop(0)
                        for line in line_dic[cur]:
                            if line not in dic:
                                dic[line] = 1
                                q.append(line)
        return ret - 1
sol = Solution()
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(sol.makeConnected(n,connections))
