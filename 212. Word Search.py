import collections
class Solution:
    def findWords(self, board, words):
        dict = collections.defaultdict(list)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                dict[board[i][j]].append([i,j])

        def helper(visited, word, cur):


            y = cur[0]
            x = cur[1]
            if y >=m or y<0 or x>=n or x<0:
                return False
            if cur in visited:
                return False
            if board[y][x] != word[len(visited)]:
                return False
            else:
                if len(visited) + 1 == len(word):
                    return True
                return helper(visited + [cur],word,[y+1, x]) or helper(visited + [cur],word,[y-1, x]) or helper(visited + [cur],word,[y, x+1]) or helper(visited + [cur],word,[y, x-1])
        ret = []
        for word in words:
            s = word[0]
            for start in dict[s]:
                if helper([], word, start):
                    ret.append(word)
                    break
        return ret



#처음 줄 때 [] "abc"
sol = Solution()
words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
board = [["a","b"],["c","d"]]

print(sol.findWords(board, words))