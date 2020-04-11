


class Solution:
    def isPossible(self, target) -> bool:
        n = len(target)
        one = [1] * n
        c = n
        """
        1일때 넘어감 
        c == target[i]면 one [i]를 교체한 후 넘어감
        c가 target[i]보다 크면 return false
        else:
            젤 문제임 one[i:]에서 하나를 뽑아 c로 바꿔야 하고 
            그래도 못미친다면 다시 반복해야댐 이 과정을 k 번 한다 치면c는
            c * 2 ^ k - 
            sum(i for i in range(k):
                2**i * one[j] j 는 랜덤
              
        """
        i = start
        while i<n and i not in visited:


sol = Solution()
target = [9,3,5]
print(sol.isPossible(target))