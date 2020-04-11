class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #palindrome axis
        dict = {}

        n = len(s)
        axis = (n-1)//2#부터 검사
        lenth = n
        sub_lenth = (lenth+1)//2
        """
        if n ==6
            axis = 0,1,2 || 3,4,5
        if n == 5:
            axis = 0,1,|2|,3,4
        """
        for i in range(axis + 1):
            dict[s[ : i + 1][::-1]] = 1

        while sub_lenth>0:

            if lenth%2 == 0:
                if s[axis + 1:axis + 1 + sub_lenth] in dict:
                    return s[axis+1:][::-1] + s[axis+1:]
                lenth +=1

            if lenth %2 == 1:
                if s[axis:axis +sub_lenth] in dict:
                    return s[axis + 1:][::-1] +s[axis] +  s[axis + 1:]
                lenth += 1

            axis -=1
            sub_lenth -= 1
        return ""
sol =Solution()
s = ""
print(sol.shortestPalindrome(s))