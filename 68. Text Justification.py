class Solution:
    def fullJustify(self, words, maxWidth: int):

        cur_length = len(words[0])
        i=1
        start = 0
        ret = []

        while i < len(words):
            cur_length += 1 + len(words[i])
            if cur_length>=maxWidth+1:
                cur_length = cur_length- 1 - len(words[i])

                end = i-1
                blank = end - start
                blank_place = maxWidth - cur_length + blank
                st = words[end]
                if not end == start:
                    for k in reversed(range(start, end)):
                        nob = blank_place//blank
                        if (k+1-start<=blank_place%blank):
                            nob += 1
                        st =  words[k] + " " *nob  + st
                else:
                    st += " " * maxWidth
                    st = st[:maxWidth]
                ret += [st]
                start = i
                cur_length= len(words[start])
                st = ""
            else:
                pass
            i += 1


        for j in range(start,len(words)):
            st += words[j] + " "
        st += " "*maxWidth
        ret+=([st[:maxWidth]])
        return ret

sol = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]


maxWidth = 20
print (sol.fullJustify(words,maxWidth))