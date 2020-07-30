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

        while num_of_task[-1][1] == 0:
            num_of_task.pop(-1)

        cur_limit =collections.defaultdict(int)
        cur_array = []
        ret = 0
        while 1:
            if not num_of_task:
                return ret
            l = len(num_of_task)
            if l <= n+1 and (num_of_task[0][0] not in cur_limit or  cur_limit[num_of_task[0][0]] == 0):

                for i in range(l):
                    num_of_task[i][1] -= 1
                while num_of_task and num_of_task[-1][1] == 0:
                    num_of_task.pop(-1)

                if num_of_task:
                    ret += n + 1
                else:
                    return ret + l
                for alpha in cur_limit:
                    cur_limit[alpha] = 0
                cur_array = []

            else:
                idx = 0
                ret+=1
                for i, e in enumerate(num_of_task):
                    alpha, num = e
                    if alpha not in cur_limit or cur_limit[alpha] == 0:
                        cur_array.append(alpha)
                        cur_limit[alpha] += 1
                        num_of_task[i][1] -= 1
                        idx = i
                        break
                if len(cur_array) > n:
                    p = cur_array.pop(0)
                    if p in cur_limit:
                        cur_limit[p] -= 1
                if num_of_task[idx][1] == 0:
                    num_of_task.pop(idx)
                elif idx<l-1 and num_of_task[idx][1] <num_of_task[idx + 1][1]:
                    num_of_task.sort(key=lambda x: -x[1])

sol = Solution()
tasks =["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"]
n =7
print(sol.leastInterval(tasks, n))