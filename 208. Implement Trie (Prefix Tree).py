class Trie:
    """
    class TreeNode():
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.balance = 0
    """
    def __init__(self):
        self.q = []

        """
        Initialize your data structure here.
        """

    def insert(self, word: str) -> None:

        if not self.q:
            self.q.append(word)
        elif len(self.q) == 1:
            t = self.q[0]
            if word < t:
                self.q.insert(0,word)
            else:
                self.q.append(word)
        else:
            l = 0
            r = len(self.q)-1
            while l < r:
                m = (l + r) // 2
                if self.q[m] <word:
                    l = m+1
                elif self.q[m] == word:
                    l = m
                    break
                elif self.q[m] > word:
                    r = m
            self.q.insert(l, word)

    def search(self, word: str) -> bool:
        if not self.q:
            return False

        else:
            l = 0
            r = len(self.q)-1
            while l < r:
                m = (l + r) // 2
                if self.q[m] <word:
                    l = m+1
                elif self.q[m] == word:
                    return True
                elif self.q[m] > word:
                    r = m
            return self.q[l] == word

    def startsWith(self, prefix: str) -> bool:
        if not self.q:
            return False
        else:
            n = len(prefix)
            l = 0
            r = len(self.q)-1
            while l < r:
                m = (l + r) // 2
                if self.q[m][:n] <prefix:
                    l = m+1
                elif self.q[m][:n] == prefix:
                    return True
                elif self.q[m][:n] > prefix:
                    r = m
            return self.q[l][:n] == prefix



s = Trie()
code = ["Trie","insert","search","search","startsWith","insert","search"]

arg = [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
out = []
for i,c  in enumerate(code[1:],1):
    if c == "insert":
        ret = s.insert(arg[i][0])
    elif c == "search":
        ret = s.search(arg[i][0])
    elif c == "startsWith":
        ret = s.startsWith(arg[i][0])
    out.append(ret)
    print(c, arg[i][0], ret)
print(out)


