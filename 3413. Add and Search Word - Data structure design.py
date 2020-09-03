class WordDictionary:

    def __init__(self):
        self.dict = self.tree()

    def addWord(self, word: str) -> None:
        cur_tree = self.dict.get_child()
        for c in word:
            idx = ord(c) - ord("a")
            if not cur_tree[idx]:
                cur_tree[idx] = self.tree()
            cur_tree = cur_tree[idx].get_child()
        cur_tree[-1] = 1
    def search(self, word: str) -> bool:
        q = [self.dict.get_child()]# 트리의 본체(self.child)를 담는다 생각
        for i, c in enumerate(word):
            if not q:
                return False
            if c == ".":
                for _ in range(len(q)):
                    t = q.pop(0)
                    for t_child in t[:26]:
                        if t_child:
                            q.append(t_child.get_child())
            else:
                idx = ord(c) - ord("a")
                for _ in range(len(q)):
                    t = q.pop(0)
                    if t[idx]:
                        q.append(t[idx].get_child())
        for t in q:
            if t[-1] == 1:
                return True
        return False
    class tree:
        def __init__(self):
            self.child = [None] * 27
        def get_child(self):
            return self.child

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
codes = ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
args = [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
dict = WordDictionary()
for c, e in zip(codes[1:],args[1:]):
    i = e[0]
    if c == "addWord":
        print(dict.addWord(i))
    elif c == "search":
        print(dict.search(i))
