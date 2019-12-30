
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        dp = [0] * N

        dp[0] = [dungeon[0][0],dungeon[0][0]]
        for i in range(M):
            for j in range(N):
                m = -999999999
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    plus = dp[j - 1][0] + dungeon[i][j]
                    dp[j] =  [plus, min(plus, dp[j-1][1])]
                elif j == 0:
                    plus = dp[j][0] + dungeon[i][j]
                    dp[j] = [plus, min(plus, dp[j][1])]
                else:
                    plus = max(dp[j-1], dp[j])
                    dp[j] = [plus[0] + dungeon[i][j], min(plus[0] + dungeon[i][j], plus[1])]
        damage = dp[-1][1]
        if damage > 0:
            return 1
        else:
            return 1 - damage

sol = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(sol.calculateMinimumHP(dungeon))
"""
#dp[i][j]는 dungeon[i][j]까지의 최대 대미지를 저장함
 i == 0 or j == 0 이면 방마다 대미지를 합한것 과 같다. 
 하지만 둘다 0이 아닌 경우
 11 정도는 최소 대미지 입은걸 구할 수 있지만
 그 외에는 현위치의 대미지에 따라, 이전에 입은 최대 대미지는 더 높지만 현재 피가 많은게 더 유리할 수 있다.
방법1
dp가 아니라 탐욕적 탐색 - 다익스트라로 품
q에 경로와 최대대미지, 현재피, 위치를 저장하고 하나 꺼낸 뒤, 가능한 경로의 최대대지미를 계산후 이것으로
정렬, 그후 다시 최소값 꺼냄
방법2

"""
