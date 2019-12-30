class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        def dict_maker(wl):
            d = {}
            for w in wl:
                for i in range(len(w)):
                    s = w[:i] + "_" + w[i+1:]
                    if s in d:
                        d[s].append(w)
                    else:
                        d[s] = [w]
            return d
        dic = dict_maker(wordList)
        not_visited = set(wordList)
        q = [[beginWord]]
        ret = []
        not_visited -= set(q)
        while q and not ret:

            for k in range(q):
                t = q.pop(0)
                for i in range(len(t)):
                    s = t[:i] + _ + t[i+1:]
                    neighbor = dic.get(s,[])
                    for n in neighbor:
                        if n == endWord:
                            ret.append(t + [n])
                        elif n in not_visited:
                            q.append(t + [n])
        return ret




sol = Solution()
begin = "hit"
end = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


print(sol.ladderLength(begin,end,wordList))