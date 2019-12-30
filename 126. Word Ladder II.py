class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList) :
        ret = []
        if endWord not in wordList:
            return ret

        wordList.insert(0, beginWord)
        differList = [[False] * len(wordList) for i in range(len(wordList))]
        def helper(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff +=1
            return diff == 1

        def finder(path):
            cur = path[-1]
            if ret:
                if len(path) > len(ret[0]):
                    return

            if wordList[cur] == endWord:
                if not ret or len(ret[0]) == len(path):
                    pass
                elif len(path) < len(ret[0]):
                    ret.clear()
                ret.append(path)
                return
            for i in range(len(differList[cur])):
                if differList[cur][i] and i not in path:
                    finder(path+[i])
                else:
                    continue
            return

        for i in range(len(wordList)):# WORD n 에서 word n 까지만  n+1은 비교 안함
            #for j in range(i+1):
            for j in range(len(wordList)):
                differList[i][j] =helper(wordList[i],wordList[j])
        finder([0])
        if not ret:
            return ret

        for i in range(len(ret)):
            for j in range(len(ret[i])):
                ret[i][j] = wordList[ret[i][j]]
        return ret


sol = Solution()
begin = "hit"
end = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.findLadders(begin,end,wordList))