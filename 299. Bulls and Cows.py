class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #bulls = strike
        #cow = ball
        exact = 0
        approx = 0
        i = 0
        B = [0] * 10
        C = [0] * 10
        while i < len(secret):
            if secret[i] == guess[i]:
                exact +=1
            B[int(secret[i])] +=1
            C[int(guess[i])] +=1
            i+=1
        for i in range(10):
            approx += min (B[i], C[i])
        approx -= exact
        return str(exact) + "A" + str(approx) + "B"

secret = "1123"
guess = "0111"
sol = Solution()
print(sol.getHint(secret, guess))