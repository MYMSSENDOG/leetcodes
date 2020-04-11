class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        while len(b)<34:
            b = b[:2] + "0" + b[2:]
        ret = 0
        for i in range(len(b)-1,1,-1):
            if b[i] == "1":
                ret += 2**(i-2)
        return ret
sol = Solution()
n = 0b00000010100101000001111010011100
print(sol.reverseBits(n))