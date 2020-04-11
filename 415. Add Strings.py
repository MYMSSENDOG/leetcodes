class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        m = 0
        if num1 == "0" and num2 == "0":
            return "0"
        temp = ""
        ret = ""
        while i >=0  or j >=0 :
            t = 0
            if i >=0:
                t += ord(num1[i])
                i -= 1
            if j>=0:
                t += ord(num2[j])
                j -= 1
            if t > 80:
                t -= 96
            else:
                t -= 48
            t += m
            r = t % 10
            temp += str(r)
            m = t // 10
        if m:
            temp += str(m)
        for c in temp[::-1]:
            ret += c
        return ret
sol = Solution()
nums1 = "1"
nums2 = "9"
print(sol.addStrings(nums1, nums2))