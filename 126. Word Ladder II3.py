from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return []
        def dict_maker(wl):
            d = {}
            for w in wl:
                for i in range(len(w)):
                    s = w[:i] + "_" + w[i + 1:]
                    if s in d:
                        d[s].append(w)
                    else:
                        d[s] = [w]
            return d
        def getLadder(start,end, t):
            if start in end:
                return [[start]]

            return [[start] + rest for x in t[start] for rest in getLadder(x,end,t)]

        dic = dict_maker(wordList)

        tree = defaultdict(set)
        tree2 = defaultdict(set)
        not_visited = set(wordList)
        q1 = {beginWord}
        q2 = {endWord}
        nq1 = set()
        nq2 = set()
        ret = []
        not_visited -= set(q1)
        not_visited -= set(q2)
        find = False
        count = 0
        while q1 and q2:
            #from start
            for word in q1:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    neighbor = dic.get(s, [])
                    for n in neighbor:
                        if n in not_visited:
                            nq1.add(n)
                            tree[word].add(n)
                        if n == endWord:
                            tree[word].add(n)
                            nq1.add(n)
                            find = True
            if nq1.intersection(q2) or nq1.intersection(nq2):
                break
            else:
                if count == 0:
                    pass
                else:
                    q2 = nq2
                    nq2 = set()
                    not_visited -= q2
            for word in q2:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    neighbor = dic.get(s, [])
                    for n in neighbor:
                        if n in not_visited:
                            nq2.add(n)
                            tree2[word].add(n)
            if nq1.intersection(q2) or nq1.intersection(nq2):
                break
            else:
                q1 = nq1
                nq1 = set()
                not_visited -= q1
                count += 1
        point = nq1.intersection(q2) or nq1.intersection(nq2)
        x = getLadder(beginWord,point,tree)
        y = getLadder(endWord,point, tree2)

        for i in x:
            for j in y:
                if i[-1] == j[-1]:
                    ret += [i + j[0:-1][::-1]]##여기만 하면됨

        return ret

#solution 1, to reduce number of branch facor, bi-directional bfs
#solution 2,


sol = Solution()
begin = "red"
end = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
print(sol.findLadders(begin, end, wordList))