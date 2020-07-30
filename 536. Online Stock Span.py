class StockSpanner:

    def __init__(self):
        self.dp = []
        self.prices = []
    def next(self, price: int) -> int:


        cur = 1
        idx = len(self.dp) - 1

        while idx >= 0:
            if self.prices[idx] <= price:
                cur += self.dp[idx]
                idx -= self.dp[idx]
            else:
                break
        self.dp.append(cur)
        self.prices.append(price)
        return self.dp[-1]




codes = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
args = [[], [100], [80], [60], [70], [60], [75], [85]]
s = StockSpanner()
for i, c in enumerate(codes[1:], 1):
    if c == "next":
        print(s.next((args[i][0])))
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)