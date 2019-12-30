class Solution:
    def exist(self, board, word: str) -> bool:
        if len(word) == 0:
            return True
        m = len(board)
        n = len(board[0])

        def find(path, s, cur_x, cur_y):
            if len(s) == 0:
                return True
            next = [[cur_x+1, cur_y],[cur_x-1, cur_y],[cur_x, cur_y+1],[cur_x, cur_y-1]]

            for step in next:
                if step in path or step[0]>m-1 or step[0]<0 or step[1] < 0 or step[1] > n-1 or board[step[0]][step[1]] != s[0]:
                    continue
                else:
                    if find(path + [step],s[1:],step[0],step[1]):
                        return True
                    else:
                        continue
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    path = [[i,j]]
                    if(find(path,word[1:],i,j)):
                        return True
        return False

sol = Solution()
board =[["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]]

word = "AAB"
print(sol.exist(board,word))