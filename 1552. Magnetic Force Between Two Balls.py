class Solution:
    def maxDistance(self, position, m: int) -> int:
        position.sort()
        start = position[0]
        end = position[-1]
        if m == 2:
            return end - start
        m -= 1
        n = len(position)
        min_diff = 1
        max_diff = (end - start) // (m) + 1
        while min_diff < max_diff:
            diff = (max_diff + min_diff) // 2
            prev = start
            count = m
            for i in range(1, n):
                if count:
                    if position[i] - prev >= diff:
                        count -= 1
                        prev = position[i]
                if not count:
                    break
            if count:
                max_diff = diff
            else:
                min_diff = diff
        return min_diff

position = [1,2,3,4,7,8,9,10,11]
m = 3
sol = Solution()
print(sol.maxDistance(position, m))
