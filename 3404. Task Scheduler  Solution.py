import collections
class Solution:
    def leastInterval(self, task, n: int) -> int:
        l = len(task)
        if n == 0:
            return l

        num_of_task = [[chr(i + 65), 0]for i in range(26)]
        for t in task:
            num_of_task[ord(t) - ord("A")][1] += 1
        num_of_task.sort(key = lambda x : -x[1])

        cur_limit =collections.defaultdict(int)
        cur_array = []
        ret = 0
        while 1:
            idx = 0
            if num_of_task[0][1] == 0:
                return ret
            for i, e in enumerate(num_of_task):
                alpha, num =  e
                if num == 0:
                    continue
                if alpha not in cur_limit or cur_limit[alpha] == 0:
                    cur_array.append(alpha)
                    cur_limit[alpha] += 1
                    num_of_task[i][1] -= 1
                    idx = i
                    break

                else:
                    continue
            else:
                cur_array.append("idle")
            ret += 1
            if len(cur_array) > n:
                p = cur_array.pop(0)
                if p in cur_limit:
                    cur_limit[p] -=1
            if len(num_of_task) > idx + 1 and num_of_task[idx][1] <num_of_task[idx + 1][1]:
                num_of_task.sort(key=lambda x: -x[1])
                while num_of_task[-1][1] == 0:
                    num_of_task.pop(-1)


sol = Solution()
tasks =["A","B","C"]
n =4
print(sol.leastInterval(tasks, n))