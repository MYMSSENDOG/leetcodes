import bisect
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo = [1,1]
        i, j = 1,1
        while i + j <= k:
            fibo.append(i+j)
            i, j = j, i+j
        count = 0
        last = len(fibo)
        while k > 0:
            idx = bisect.bisect_right(fibo[:last], k)
            last = idx
            k -= fibo[last - 1]
            count +=1
        return count


sol = Solution()
k = 19
print(sol.findMinFibonacciNumbers(k))