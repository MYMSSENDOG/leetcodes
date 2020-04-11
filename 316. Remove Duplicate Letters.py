import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = collections.defaultdict(list)
        for i, c in enumerate(s):
            d[c] +=[i]

        ret = [""] * len(s)
        smallest = "z"
        idx = 0
        while d:
            c = s[idx]
            if c in d:
                smallest = min(smallest, c)
            else:
                idx +=1
                continue

            if idx == d[c][-1]:
                ret[d[smallest][0]] = smallest
                d.pop(smallest)
                idx =0
                smallest = "z"
            else:
                idx+=1
        return ret


sol = Solution()
s = "bcabc"
print(sol.removeDuplicateLetters(s))


"""
문제의 법칙들
1. a는 무조건 제일 왼쪽 z 는 무조건 제일 오른쪽
2. 하나만 있는거는 바로 그자리
3. 알파벳의 위치가 확정되는 순간
    하나만 있을때
    다른 모든 것이 확정 되었을때, 자신의 위치 전부?를 비교해보면 됨
        후보위치들의 왼쪽부터 시작해서 lexicographical 값이 작아진다면 거기에 바로 넣으면 될듯
        즉 오른쪽 무언가보다 자신의 값이 작으면 됨
    n개가 확정이 되었어도 다른 것에 따라 변동할 가능성이 있다  오름차순으로 할 시
    내림차순도 비슷 한 것같다
    즉 한번에 하거나 여러개에서 하나를 뽑거나 할때마다 수정을 하거나
     
    
         


"""