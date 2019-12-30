import copy
class Solution:
    def combinationSum2(self, candidates, target):
        ret = []
        def solve(i, target, answer):
            if target == 0:
                temp = copy.deepcopy(answer)
                temp.sort()
                if temp not in ret:
                    ret.append(temp)
                    return
            elif target<0 or i == len(candidates):
                return
            for j in range(len(candidates[i + 1:])):
                answer.append(candidates[i + 1:][j])
                solve (i + j +  1, target-candidates[i + 1:][j],answer)
                answer.pop()

        for i in range(len(candidates)):
            answer = [candidates[i]]
            solve(i,target - candidates[i], answer)

        return ret
candidates = [2,5,2,1,2]
target = 5
sol = Solution()
print(sol.combinationSum2(candidates,target))
