import collections
class WordDictionary:

    def __init__(self):
        self.q = []
        self.dict = {}

    def addWord(self, word: str) -> None:
        if word not in dict:
            dict[word] = 1
            self.q.append(word)

    def search(self, word: str) -> bool:
        for w in self.q:
            if len(w) != len(word):
                continue
            else:
                find = True
                for i in range(len(w)):
                    if w[i] == word[i] or word[i] == ".":
                        continue
                    else:
                        find = False
                        break
                if find:
                    return True
        return False