import collections
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        d = collections.defaultdict(int)
        q =[(sr, sc)]
        m, n = len(image), len(image[0])
        cur_color = image[sr][sc]
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        while q:
            for _ in range(len(q)):
                r, c = q.pop(0)

                if image[r][c] != cur_color or (r, c) in d:
                    continue
                d[(r, c)] = 1
                image[r][c] = newColor
                for y, x in dirs:
                    if 0 <= r+y<m and 0<= c + x < n:
                        q.append((r+y, c+x))
        return image



image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
sol = Solution()
print(sol.floodFill(image,sr,sc, newColor))