class Solution:
    def distributeCandies(self, candies: int, n: int):
        ret = [0] * n
        a = n**2
        b = n
        c = -2 * candies
        r = int((-b + (b**2 - 4 * a * c) ** (1/2)) // (2 * a))



        for i in range(n):
            ret[i] += (i + 1) * r + n * (r - 1) * (r) // 2
        candies -= (r * n + r**2 * n**2)//2
        for i in range(n):
            k = min(r*n + i + 1, candies)
            ret[i] += k
            candies -= k
            if not candies:
                break
        return ret




sol = Solution()
candies = 7
num_people = 4
print(sol.distributeCandies(candies, num_people))