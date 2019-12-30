def put(stack_num_list, stack_dic,stack, i):
    stack_num_list.append(stack)
    if stack in stack_dic:
        stack_dic[stack].append(i)
    else:
        stack_dic[stack] = [i]

def isValidBetween(stack_num_list,i,j):
    if i >= j:
        return 0
    k = i
    tmp = stack_num_list[i]
    while k < j + 1:
        if stack_num_list[k] < tmp:
            return False
        k += stack_num_list[k] - tmp if stack_num_list[k] - tmp != 0 else 1
    return True

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        #(까지 간뒤 , 유효할때까지 계속 가서
        #끝에서 몇갠지 구한다.
        n = len(s)
        stack = 0
        longest = 0
        stack_num_list = []
        stack_start_dic = {}
        stack_end_dic = {}
        for i,p in enumerate(s):#순서일부러 다르게함
            if p == "(":
                put(stack_num_list, stack_start_dic,stack, i)
                stack +=1

            else:
                stack -= 1
                put(stack_num_list, stack_end_dic,stack, i)
        for idx_of_stack_num_list in stack_start_dic:

            if idx_of_stack_num_list not in stack_end_dic:
                continue
            if len(stack_start_dic[idx_of_stack_num_list]) + len(stack_end_dic[idx_of_stack_num_list])<2:
                continue
            stack_end_dic[idx_of_stack_num_list].reverse()
            for i in stack_start_dic[idx_of_stack_num_list]:
                if n - i < longest :
                    break


                for j in stack_end_dic[idx_of_stack_num_list]:
                    if j - i + 1 < longest:
                        break
                    if isValidBetween(stack_num_list,i,j):
                        longest = max(longest, j-i + 1)
                        break
        if longest%2 == 1:
            longest-=1
        return longest



sol = Solution()
s = ")(()))()(())()()()()(()(()))()())(()()(())()(((()()(()((()(()()((()()))(())())(()(())(()(())(()(()))(()))()()(((()())(()()(()((())))))(()(()())(()))))))())))()())()(())(((()(()))()()(()(((()))()"
print(sol.longestValidParentheses(s))