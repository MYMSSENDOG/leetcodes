class Solution:
    def maxProfit(self, prices) -> int:
        first = 0
        second = 0
        #1번방법 변수4개 n^4
        #스트링을 2번 두개로 나눠서 함 n^2
        #피크와 로우만 추려서 함 이역시 n^2이긴 하지만 약간 절약은 될듯
        #2개로 나누고 하나씩 진행하면서 왼쪽은 is min? else max = this - min
        #오른쪽은 음...
        array = [0] * len(prices)
        min_price = 9999999
        ret = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                if prices[i] - min_price > ret:
                    ret = prices[i] - min_price
            array[i] = ret
        top_price = -1
        ret = 0
        for i in reversed(range(1,len(prices))):
            if prices[i] > top_price:
                top_price = prices[i]
            else:
                if top_price - prices[i] > ret:
                    ret = top_price - prices[i]
            array[i-1] += ret
        return max(array)

sol = Solution()
prices = [7,11,4,1,2]
print(sol.maxProfit(prices))