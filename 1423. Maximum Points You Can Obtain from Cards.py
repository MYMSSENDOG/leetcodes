class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        s = sum(cardPoints)

        k = len(cardPoints) - k
        S = sum(cardPoints[:k])
        m = S
        for i in range(k, len(cardPoints)):
            S = S + cardPoints[i] - cardPoints[i-k]
            m = min(m, S)
        return s - m

sol = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(sol.maxScore(cardPoints,k))