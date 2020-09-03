class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # no re-use
        memo = {}
        def helper(sum, rest):
            state = tuple(rest)
            if state in memo:
                return memo[state]
            else:
                memo[state] = False
                if max(rest) + sum >= desiredTotal:
                    memo[state] = True
                else:
                    for y in rest:
                        next_rest =[i for i in rest if i != y]
                        if helper(sum + y, next_rest) == False:
                            memo[tuple(state)] = True
                            break
                return memo[state]


        if maxChoosableInteger * (maxChoosableInteger +1) // 2 < desiredTotal:
            return False
        array = [i+1 for i in range(maxChoosableInteger)]
        return helper(0, array)
        #다음 스텝에 상대방이 하나라도 False가 되는것이 있다면 무조건나는 True 상대가
        #다음스텝에 all True라면 나는 False
        

sol = Solution()
maxChoosableInteger = 8
desiredTotal = 10
print(sol.canIWin(maxChoosableInteger, desiredTotal))