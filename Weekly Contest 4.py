class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_pos(alpha):
            n = ord(alpha) - ord("A")
            x = n //6
            y = n % 6
            return [x,y]
        dic = {}
        for i in range(ord("A"), ord("Z") + 1):
            dic[chr(i)] = get_pos(chr(i))
        ret = 0

        f1 = dic[word[0]]
        for w in word[1:]:


sol = Solution()
word = "CAKE"
print(sol.minimumDistance(word))