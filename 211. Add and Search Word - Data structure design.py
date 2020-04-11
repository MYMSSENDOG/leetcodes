import collections
class WordDictionary:

    def __init__(self):
        self.dic = collections.defaultdict(set)
        self.words = set()
        self.len_dict = {}
        # case 1 lot of space, lot of time but search O91)
        #just note all of capable word in dictionary for example input word is "abc"
        #record ".bc" "a.c" "ab." "a.." ...
        #it work within O(2**s) time and O(2**s) space but search(1)

        #case 2  use just 1 char
        # input = "abc"  record "a.." -> "abc" ".b." -> "abc"...
        #in search, time complexity is O(s) addword is (s**2) space is (s**2)

        #case3 just use array
        #space s time 1 but search worst case is n(num of word) * s


    def addWord(self, word: str) -> None:
        for i in range(len(word)):
            t = "." * i + word[i] + "." * (len(word) - (i + 1))
            self.dic[t].add(word)
        self.words.add(word)
        self.len_dict[len(word)] = 1
    def search(self, word: str) -> bool:
        s = self.words
        if word.count(".") == len(word):
            return len(word) in self.len_dict
        for i in range(len(word)):
            if word[i] != ".":
                t = "." * i + word[i] + "." * (len(word) - (i + 1))
                s = self.dic[t].intersection(s)

        if s:
            return True
        else:
            return False

d = WordDictionary()
code = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
arg = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
for i,e in enumerate(code[1:],1):
    t = arg[i][0]
    if e == "addWord":
        print(d.addWord(t))
    elif e == "search":
        print(d.search(t))
    print(t, e)

"""
to search in O(1)
save all possible combinations of word
ex) word = "abc"
dic = {}
dic_w = [".bc", "a.c", "ab.", "a..", ".b.", "..c", "...", "abc"]
add O(W**2)

d = number of "."
n = number of words
to search in O(n*d)
add O(W)
 
"""