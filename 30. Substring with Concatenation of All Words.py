"""
def find_starting_point(s, words,start):
    min = len(s)
    for word in words:
        find = s.find(word,start)
        if find>=0:
            if find<min:
                min = find
            else:
                continue
    return min

def find_starting_point2(s, words):
    s_list = []
    start = 0
    words = set(words)
    words = list(words)
    for word in words:
        start = 0
        while start + len(word) <= len(s):
            find = s.find(word,start)
            if find< 0:
                break
            else:
                s_list.append(find)
                start = find + 1
    return s_list

class Solution:
    def findSubstring(self, s, words):


        words_num = len(words)
        all_words_len = 0
        for word in words:
            all_words_len += len(word)
        ret = []
        cur_idx = 0
        start = 0
        s_list = find_starting_point2(s, words)
        s_list = set(s_list)
        s_list = list(s_list)
        s_list.sort()

        s_list_index = 0

        while start +  all_words_len <= len(s):
            used_idx = [1] * words_num
            used_num = 0
            if s_list_index >= len(s_list):
                break
            cur_idx = s_list[s_list_index]
            s_list_index += 1


            start = cur_idx
            while used_num < len(words):
                is_match = False
                for w_idx, word in enumerate(words):
                    # 만약 검사 한거면 넘ㄴ어감
                    if used_idx[w_idx] == 0:
                        continue
                    wl = len(word)
                    #이번 단어가 있다면 이번거 찾았다고 표시, 비활성화, 갯수하나 추가
                    if s.find(word,cur_idx,cur_idx + wl) >= 0:
                        used_num+=1
                        used_idx[w_idx] = 0
                        cur_idx += wl
                        is_match = True
                if is_match == False:
                    break# 이번 while을 나간다 다음 스타팅 포인트를 찾는다.
            if used_num == len(words):
                ret.append(start)
        return ret
        """
"""
        while cur_idx +  all_words_len <= len(s):
            used_idx = [1] * words_num
            used_num = 0
            cur_idx = find_starting_point(s,words,start)
            start = cur_idx
            while used_num < len(words):
                is_match = False
                for w_idx, word in enumerate(words):
                    # 만약 검사 한거면 넘ㄴ어감
                    if used_idx[w_idx] == 0:
                        continue
                    wl = len(word)
                    #이번 단어가 있다면 이번거 찾았다고 표시, 비활성화, 갯수하나 추가
                    if s.find(word,cur_idx,cur_idx + wl) >= 0:
                        used_num+=1
                        used_idx[w_idx] = 0
                        cur_idx += wl
                        is_match = True
                if is_match == False:
                    break# 이번 while을 나간다 다음 스타팅 포인트를 찾는다.
            if used_num == len(words):
                ret.append(start)
            start = cur_idx
        return ret
"""
class Solution:
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans

sol = Solution()

s = "asdqwezxczxcasdqwe"
words = ["asd","zxc","qwe"]
print(sol.findSubstring(s, words))