class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        ret = []
        if endWord not in wordList:
            return ret

        wordList.insert(0, beginWord)
        m = len(wordList)
        differList = [[False] * len(wordList) for i in range(m)]
        idx = wordList.index(endWord)
        def helper(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff +=1
            return diff == 1
        for i in range(m):
            #for j in range(i+1):
            for j in range(m):
                differList[i][j] =helper(wordList[i],wordList[j])
        q = [[0]]
        while q:
            for i in range(len(q)):
                t = q.pop(0)#t는 현재 워드 넘버
                for j in range(m):
                    if differList[t[-1]][j] and j not in t:
                        if j == idx:
                            ret.append(t+[j])
                        else:
                            q.append(t + [j])
            if ret:
                break
        for i in range(len(ret)):
            for j in range(len(ret[i])):
                ret[i][j] = wordList[ret[i][j]]
        return ret



sol = Solution()
begin = "a"
end = "c"
wordList = ["a","b","c"]
print(sol.findLadders(begin, end, wordList))