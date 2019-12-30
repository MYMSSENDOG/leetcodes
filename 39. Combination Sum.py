import copy
class Solution:
    def combinationSum(self, candidates, target) :
        ret = []
        def solve(i, target, answer):
            if target == 0:

                ret.append(copy.deepcopy(answer))

                return
            elif target < 0 or candidates[i]> target:
                return

            for j in range(len(candidates[i:])):
                answer.append(candidates[i:][j])
                solve (i + j, target-candidates[i:][j],answer)
                answer.pop()

        for i in range(len(candidates)):
            answer = [candidates[i]]
            solve(i,target - candidates[i], answer)
        return ret



sol = Solution()
print(sol.combinationSum([2,3,5],8))
