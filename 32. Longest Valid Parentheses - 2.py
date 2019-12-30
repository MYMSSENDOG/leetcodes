class Solution:
    def longestValidParentheses(self, s: str) -> int:

        right = 0
        left = 0
        maximum = 0
        for i in s:
            if i == "(" :
                left += 1
            else:
                right += 1
                if right == left:
                    maximum = max(right * 2, maximum)
                elif right>left:
                    right = 0
                    left = 0

        right = 0
        left = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == "(" :
                left += 1
                if right == left:
                    maximum = max(right * 2, maximum)
                elif right<left:
                    right = 0
                    left = 0
            else:
                right += 1

        return maximum


sol = Solution()
s = ")(()))()(())()()()()(()(()))()())(()()(())()(((()()(()((()(()()((()()))(())())(()(())(()(())(()(()))(()))()()(((()())(()()(()((())))))(()(()())(()))))))())))()())()(())(((()(()))()()(()(((()))()"
print(sol.longestValidParentheses(s))