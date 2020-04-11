class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight




class Solution:
    def construct(self, grid):

        def helper(y,x,n):
            val = grid[y][x]
            is_leaf = True
            if n == 1:
                return Node(val, True, None,None,None,None)
            else:
                for b in range(y, y+n):
                    if not is_leaf:
                        break
                    for a in range(x, x+n):
                        if grid[b][a] != val:
                            is_leaf = False
                            break
                if is_leaf:
                    return Node(val, True, None,None,None,None)
                else:
                    dist = n//2
                    return Node(1, False, helper(y,x,dist), helper(y,x + dist,dist),helper(y + dist,x ,dist) , helper(y + dist,x + dist,dist))

        root =  helper(0,0,len(grid))
        return root


sol = Solution()
grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
print(sol.construct(grid))